# -*- coding: utf-8 -*-
from tools.core import Configuration
from ca.core import CertificateAuthority
from server.core import Server
import print_pems as ppems

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME  = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME   = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME      = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME  = RESOURCES_DIR + "server-public-key.pem"

CA_PASSWORD     = "ca_secret_password"
SERVER_PASSWORD = "server_secret_password"

CA_CONFIGURATION = Configuration(
    "FR", "Territoire de Belfort", "Sevenans", "UTBM_CA", "localhost"
)
SERVER_CONFIGURATION = Configuration(
    "FR", "Territoire de Belfort", "Sevenans", "UTBM_SER", "localhost",
    alt_names=["localhost"]
)

# Étapes 1 et 2 — Création de l'autorité de certification
certificate_authority = CertificateAuthority(
    CA_CONFIGURATION,
    CA_PASSWORD,
    CA_PRIVATE_KEY_FILENAME,
    CA_PUBLIC_KEY_FILENAME
)

# Étapes 3 et 4 — Création du serveur (clé privée + CSR)
server = Server(
    SERVER_CONFIGURATION,
    SERVER_PASSWORD,
    SERVER_PRIVATE_KEY_FILENAME,
    SERVER_CSR_FILENAME
)

# Étape 5 — Signature du certificat serveur par la CA
certificate_authority.sign(server.get_csr(), SERVER_PUBLIC_KEY_FILENAME)

# Affichage des certificats générés
print("=== CA Public Key ===")
ppems.print_perms(CA_PUBLIC_KEY_FILENAME)

print("=== Server CSR ===")
ppems.print_perms(SERVER_CSR_FILENAME)

print("=== Server Public Key (signed by CA) ===")
ppems.print_perms(SERVER_PUBLIC_KEY_FILENAME)

print("finished ...")
