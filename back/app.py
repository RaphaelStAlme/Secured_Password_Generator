import random
import string
import hashlib
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a route for generating secure passwords.
@app.route('/generate_password', methods=['GET'])
def generate_password():
    # Get query parameters from the request.
    args = request.args
    # Extract the desired length of the password (default is 8 characters).
    length = int(args.get('length', 8))
    # Determine whether to include digits in the password.
    digits = args.get('digits', 'true').lower() == 'true'
    # Determine whether to include symbols in the password.
    symbols = args.get('symbols', 'true').lower() == 'true'
    # Determine whether to hash the generated password.
    hash_option = args.get('hash', 'false').lower() == 'true'

    # Define the character set for generating passwords.
    chars = string.ascii_uppercase + string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    # Generate a random password of the specified length.
    password = ''.join(random.choice(chars) for _ in range(length))

    # If the hash option is enabled, hash the generated password.
    if hash_option:
        password = hash_password(password)
    
    # Return the generated password in JSON format.
    return jsonify({"password": password})

# Define a function for hashing a password using SHA-256.
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    app.run(debug=True, port=5000)