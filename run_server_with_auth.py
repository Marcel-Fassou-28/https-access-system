# -*- coding: utf-8 -*-
"""
Partie 5 : Améliorations — Authentification utilisateur avec mot de passe hashé
"""
import hashlib
import os
import ssl
from flask import Flask, request, Response

SECRET_MESSAGE = "hypsilophodon"
SERVER_PASSWORD = "server_secret_password"
app = Flask(__name__)

# --- Gestion des utilisateurs ---
# Les mots de passe sont stockés sous forme de hash SHA-256 + sel (salt)
# Ne JAMAIS stocker les mots de passe en clair !

def hash_password(password: str, salt: str) -> str:
    """Hache un mot de passe avec un sel (SHA-256)."""
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()

# Génération d'un sel unique par utilisateur
SALT_ALICE = os.urandom(16).hex()
SALT_BOB   = os.urandom(16).hex()

USERS = {
    "alice": {"salt": SALT_ALICE, "hashed_pw": hash_password("alice123", SALT_ALICE)},
    "bob":   {"salt": SALT_BOB,   "hashed_pw": hash_password("bob456",   SALT_BOB)},
}


def check_auth(username: str, password: str) -> bool:
    """Vérifie les credentials d'un utilisateur."""
    user = USERS.get(username)
    if user is None:
        return False
    return hash_password(password, user["salt"]) == user["hashed_pw"]


def require_auth():
    """Renvoie une réponse 401 pour déclencher l'authentification HTTP Basic."""
    return Response(
        "Accès refusé. Authentification requise.",
        401,
        {"WWW-Authenticate": 'Basic realm="Club privé"'}
    )


@app.route("/")
def get_secret_message():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return require_auth()
    return f"Bienvenue {auth.username} ! Le mot de passe du club est : {SECRET_MESSAGE}"


if __name__ == "__main__":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
        certfile="resources/server-public-key.pem",
        keyfile="resources/server-private-key.pem",
        password=SERVER_PASSWORD,
    )
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8081,
        ssl_context=ssl_context,
    )