from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your tests here.

class TestHome(LiveServerTestCase):
    browser = webdriver.Chrome()
   
    def test_login(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert 'Login' in self.browser.title
        
        