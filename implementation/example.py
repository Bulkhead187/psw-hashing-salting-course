```python
import bcrypt

# Step 1: Generate a salt
salt = bcrypt.gensalt()

# Step 2: Hash the password with the salt
password = "superSecretPassword"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

print(f"Salted and Hashed Password: {hashed_password}")
