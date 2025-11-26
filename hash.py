from werkzeug.security import generate_password_hash

password = "admin"

hashed_password = generate_password_hash(password)

print("Original Password:", password)
print("Encrypted Password:", hashed_password)
