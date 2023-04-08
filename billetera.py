import ecdsa
import os

# Generar clave privada
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

# Generar clave pública
public_key = private_key.get_verifying_key()

# Obtener la dirección de la billetera a partir de la clave pública
address = public_key.to_string().hex()

print("Private key:", private_key.to_string().hex())
print("Public key:", public_key.to_string().hex())
print("Address:", address)
