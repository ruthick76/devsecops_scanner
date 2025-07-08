import os

# Hardcoded credentials (Bandit will flag this)
USERNAME = "admin"
PASSWORD = "password123"

# Dangerous function usage
eval("print('This is insecure')")

# Weak cryptography (Bandit will flag this too)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = b'0000000000000000'
cipher = Cipher(algorithms.AES(key), modes.ECB())
