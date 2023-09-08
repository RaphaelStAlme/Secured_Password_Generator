import unittest
import time
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestFront(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.ChromiumEdge()
        self.driver.get("http://localhost:4321")

    def test_home_page(self):
        time.sleep(1)

    def test_generate_basic_password(self):
        passwordLengthElement = self.driver.find_element(
            By.ID, "passwordLength")
        passwordLengthElement.send_keys(Keys.ENTER)
        generatedPasswordElement = self.driver.find_element(
            By.ID, "generatedPassword")
        time.sleep(0.500)
        self.assertEqual(generatedPasswordElement.text.__len__(), 8)

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

    @classmethod
    def setDownClass(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
