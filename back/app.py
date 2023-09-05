
import random
import string
from flask import Flask

app = Flask(__name__)

@app.route('/generate_password')

def generate_password():
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return password

if __name__ == '__main__':
    app.run(debug=True, port=5000)
