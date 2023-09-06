
import random
import string
import hashlib
from flask import Flask, jsonify, request
from flask_cors import CORS

# Program in Python that generates secure passwords while offering a
# customization to the user. The program will allow the user to specify
# the desired length of the password in characters and to choose whether to include numbers or
# symbols. In addition, optionally, you can integrate a
# hashing feature using an encryption algorithm of your choice.
app = Flask(__name__)
CORS(app)

@app.route('/generate_password', methods=['GET'])
def generate_password():
    args = request.args
    length = int(args.get('length', 8))
    digits = args.get('digits', 'true').lower() == 'true'
    symbols = args.get('symbols', 'true').lower() == 'true'
    hash = args.get('hash', 'false').lower() == 'true'

    chars = string.ascii_uppercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    if hash:
        password = hash_password(password)
    return jsonify(password)

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
