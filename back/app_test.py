import unittest
import random
import string
import hashlib
import json

def generate_password(length, digits, symbols, hash):
    chars = string.ascii_uppercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    if hash:
        password = hash_password(password)
    return json.dumps(password)

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def length_password(password):
    return len(password) -2

class TestApp(unittest.TestCase):
    def test_generate_password(self):
        password = generate_password(8, True, True, True)
        self.assertEqual(length_password(password), 64)

    def test_generate_password_without_digits(self):
        password = generate_password(8, False, True, True)
        self.assertEqual(length_password(password), 64)

    def test_generate_password_without_symbols(self):
        password = generate_password(8, True, False, True)
        self.assertEqual(length_password(password), 64)

    def test_generate_password_without_hash(self):
        password = generate_password(8, True, True, False)
        self.assertEqual(length_password(password), 8)

    def test_generate_password_without_hash_and_length_of_0(self):
        password = generate_password(0, True, True, False)
        self.assertEqual(length_password(password), 0)

    def test_generate_password_without_hash_and_length_of_1(self):
        password = generate_password(1, True, True, False)
        self.assertEqual(length_password(password), 1)

    def test_generate_password_without_hash_and_length_negative(self):
        password = generate_password(-1, True, True, False)
        self.assertEqual(length_password(password), 0)

    def test_hash_password(self):
        password = hash_password('test')
        self.assertEqual(length_password(password), 62)

if __name__ == '__main__':
    unittest.main()
