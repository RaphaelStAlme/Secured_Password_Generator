# Import necessary modules and libraries
import unittest
import time
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Define a test class that inherits from unittest.TestCase
class TestFront(unittest.TestCase):

    # Class-level setup method to initialize the web driver and open a webpage
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.ChromiumEdge()
        self.driver.get("http://localhost:4321")

    # Test method: Check the home page and wait for 1 second
    def test_home_page(self):
        time.sleep(1)

    # Test method: Generate a basic password and check its length
    def test_generate_basic_password(self):
        passwordLengthElement = self.driver.find_element(
            By.ID, "passwordLength")
        passwordLengthElement.send_keys(Keys.ENTER)
        generatedPasswordElement = self.driver.find_element(
            By.ID, "generatedPassword")
        time.sleep(0.500)
        self.assertEqual(generatedPasswordElement.text.__len__(), 8)

    # Test method: Generate a password with digits, check length, and regex for digits
    def test_generate_password_with_digits(self):
        self.driver.refresh()
        passwordLengthElement = self.driver.find_element(
            By.ID, "passwordLength")
        digitsElement = self.driver.find_element(By.ID, "digits")
        digitsElement.click()
        passwordLengthElement.clear()
        passwordLengthElement.send_keys(12)
        passwordLengthElement.send_keys(Keys.ENTER)
        generatedPasswordElement = self.driver.find_element(
            By.ID, "generatedPassword")
        self.assertEqual(generatedPasswordElement.text.__len__(), 12)
        self.assertRegex(generatedPasswordElement.text, r'[0-9]')
        time.sleep(0.500)

    # Test method: Generate a password with symbols, check length, and regex for symbols
    def test_generate_password_with_symbols(self):
        self.driver.refresh()
        passwordLengthElement = self.driver.find_element(
            By.ID, "passwordLength")
        symbolsElement = self.driver.find_element(By.ID, "symbols")
        symbolsElement.click()
        passwordLengthElement.clear()
        passwordLengthElement.send_keys(12)
        passwordLengthElement.send_keys(Keys.ENTER)
        generatedPasswordElement = self.driver.find_element(
            By.ID, "generatedPassword")
        self.assertEqual(generatedPasswordElement.text.__len__(), 12)
        self.assertRegex(generatedPasswordElement.text, r'[^A-Za-z0-9]')
        time.sleep(0.500)

    # Test method: Generate a password with digits and symbols, check length, and regex
    def test_generate_password_with_digits_symbols(self):
        self.driver.refresh()
        passwordLengthElement = self.driver.find_element(
            By.ID, "passwordLength")
        digitsElement = self.driver.find_element(By.ID, "digits")
        symbolsElement = self.driver.find_element(By.ID, "symbols")
        digitsElement.click()
        symbolsElement.click()
        passwordLengthElement.clear()
        passwordLengthElement.send_keys(12)
        passwordLengthElement.send_keys(Keys.ENTER)
        generatedPasswordElement = self.driver.find_element(
            By.ID, "generatedPassword")
        self.assertEqual(generatedPasswordElement.text.__len__(), 12)
        self.assertRegex(generatedPasswordElement.text, r'[0-9]')
        self.assertRegex(generatedPasswordElement.text, r'[^A-Za-z0-9]')
        time.sleep(0.500)

    # Test method: Generate a password with a hash, check length
    def test_generate_password_with_hash(self):
        self.driver.refresh()
        passwordLengthElement = self.driver.find_element(
            By.ID, "passwordLength")
        digitsElement = self.driver.find_element(By.ID, "digits")
        symbolsElement = self.driver.find_element(By.ID, "symbols")
        hashElement = self.driver.find_element(By.ID, "hash")
        digitsElement.click()
        symbolsElement.click()
        passwordLengthElement.clear()
        passwordLengthElement.send_keys(12)
        hashElement.click()
        passwordLengthElement.send_keys(Keys.ENTER)
        generatedPasswordElement = self.driver.find_element(
            By.ID, "generatedPassword")
        self.assertEqual(generatedPasswordElement.text.__len__(), 64)
        time.sleep(0.500)

    # Test method: Generate a password and check if it's copied to the clipboard
    def test_generate_password_in_clipboard(self):
        self.driver.refresh()
        passwordLengthElement = self.driver.find_element(
            By.ID, "passwordLength")
        digitsElement = self.driver.find_element(By.ID, "digits")
        symbolsElement = self.driver.find_element(By.ID, "symbols")
        hashElement = self.driver.find_element(By.ID, "hash")
        digitsElement.click()
        symbolsElement.click()
        passwordLengthElement.clear()
        passwordLengthElement.send_keys(12)
        hashElement.click()
        passwordLengthElement.send_keys(Keys.ENTER)
        generatedPasswordElement = self.driver.find_element(
            By.ID, "generatedPassword")
        root = tk.Tk()
        root.withdraw()
        clipboardText = root.clipboard_get()
        self.assertEqual(clipboardText, generatedPasswordElement.text)
        time.sleep(0.500)

    # Class-level teardown method to close the web driver
    @classmethod
    def setDownClass(self):
        self.driver.close()

# Entry point to run the test suite
if __name__ == "__main__":
    unittest.main()