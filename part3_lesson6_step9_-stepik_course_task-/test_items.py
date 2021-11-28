from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import math
import time
import pytest


link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_button(browser):
    browser.get(link)
    time.sleep(30)
    button=browser.find_elements(By.CSS_SELECTOR,'[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button is not None, "NO BUTTON \"Add-to-basket\""