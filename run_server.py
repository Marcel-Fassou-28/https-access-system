# -*- coding: utf-8 -*-
import ssl
from flask import Flask

SECRET_MESSAGE = "hypsilophodon"  # Modifier ici pour la Partie 1
SERVER_PASSWORD = "server_secret_password"
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":
    # HTTP version (Partie 1)
    # app.run(debug=True, host="0.0.0.0", port=8081)

    # HTTPS version (Partie 4)
    # Les fichiers server-public-key.pem et server-private-key.pem doivent
    # être présents dans le répertoire resources/
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