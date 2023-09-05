import secrets

# Generate a secure random secret key
secret_key = secrets.token_hex(16)  # 16 bytes (128 bits)

print(secret_key)
