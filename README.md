# HTTPS ACCESS SYSTEM

Projet de sécurisation d'un portail d'accès pour un club privé en remplaçant une communication HTTP non sécurisée par une connexion HTTPS basée sur une infrastructure à clés publiques (PKI).

## Objectif

Le mot de passe mensuel du club était distribué via un serveur HTTP, ce qui permettait à un attaquant observant le trafic réseau de lire les informations échangées en clair.

L'objectif du projet est de :

* Générer une autorité de certification (CA) locale.
* Créer et signer un certificat serveur.
* Mettre en place un serveur HTTPS avec Flask.
* Sécuriser la transmission du mot de passe du club.
* Ajouter une authentification utilisateur avec stockage sécurisé des mots de passe.

## Fonctionnalités

* Génération d'une clé privée RSA 2048 bits pour la CA.
* Création d'un certificat X.509 autosigné.
* Génération d'une clé privée serveur et d'une CSR.
* Signature du certificat serveur par la CA.
* Serveur Flask accessible en HTTPS.
* Authentification HTTP Basic.
* Hachage des mots de passe avec SHA-256 et sel aléatoire.

## Structure du projet

```text
ca/
server/
tools/
resources/
run_server.py
run_server_with_auth.py
build.py
```

## Utilisation

### Installation

```bash
git clone https://github.com/Marcel-Fassou-28/https-access-system
cd https-access-system
python -m venv venv
pip install -r requirements
```

### Générer les certificats

```bash
python build.py
```

### Lancer le serveur HTTPS

```bash
python run_server.py
```

### Lancer le serveur avec authentification

```bash
python run_server_with_auth.py
```

## Remarque

Le navigateur peut afficher un avertissement de sécurité car le certificat est signé par une autorité locale non reconnue. Pour supprimer cet avertissement, il est nécessaire d'ajouter le certificat de la CA au magasin de certificats de confiance ou d'utiliser une autorité reconnue publiquement (ex. Let's Encrypt).

## Technologies

* Python
* Flask
* OpenSSL / Cryptography
* RSA 2048 bits
* X.509
* HTTPS / TLS
* Wireshark
