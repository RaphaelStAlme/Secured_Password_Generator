import string
import unittest
from app import app

# Define a test class for the Flask application.
class TestApp(unittest.TestCase):

    # Set up the test environment.
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # Step 0 : Test generating a hashed password (SHA-256).
    def test_generate_password_hashed(self):
        response = self.app.get('/generate_password?hash=true')
        data = response.get_json()
        password = data['password']
        self.assertEqual(len(password), 64)  # SHA-256 hashed password

    # Step 1 : Test generating a non-hashed password.
    def test_generate_password_not_hashed(self):
        response = self.app.get('/generate_password?hash=false')
        data = response.get_json()
        password = data['password']
        self.assertEqual(len(password), 8)

    # Step 2 : Test generating a password with the default length (8 characters).
    def test_generate_password_default_length(self):
        response = self.app.get('/generate_password')
        data = response.get_json()
        password = data['password']
        self.assertEqual(len(password), 8)

    # Step 3 : Test generating a password with a custom length (12 characters).
    def test_generate_password_custom_length(self):
        response = self.app.get('/generate_password?length=12')
        data = response.get_json()
        password = data['password']
        self.assertEqual(len(password), 12)
    
    # Step 4 : Test generating a password with a null length (0 characters).
    def test_generate_password_null_length(self):
        response = self.app.get('/generate_password?length=0')
        data = response.get_json()
        password = data['password']
        self.assertEqual(len(password), 0)

    # Step 5 : Test generating a password with symbols included.
    def test_generate_password_with_symbols(self):
        response = self.app.get('/generate_password?symbols=true')
        data = response.get_json()
        password = data['password']
        self.assertTrue(any(c in string.punctuation for c in password))

    # Step 6 : Test generating a password without symbols.
    def test_generate_password_without_symbols(self):
        response = self.app.get('/generate_password?symbols=false')
        data = response.get_json()
        password = data['password']
        self.assertTrue(all(c.isalpha() or c.isdigit() for c in password))

    # Step 7 : Test generating a password with digits included.
    def test_generate_password_with_digits(self):
        response = self.app.get('/generate_password?digits=true')
        data = response.get_json()
        password = data['password']
        self.assertTrue(any(c.isdigit() for c in password))

    # Step 8 : Test generating a password without digits.
    def test_generate_password_without_digits(self):
        response = self.app.get('/generate_password?digits=false')
        data = response.get_json()
        password = data['password']
        self.assertTrue(all(c.isalpha() or c in string.punctuation for c in password))  

if __name__ == '__main__':
    unittest.main()