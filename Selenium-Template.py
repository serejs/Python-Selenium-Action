from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup as bs4
import mysql.connector
import re

# Configura il percorso di Chrome
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--remote-debugging-port=9222')  # Specify a port
options.add_argument('--disable-setuid-sandbox')

options.add_argument("--incognito")
options.add_argument("--disable-application-cache")
options.add_argument("--enable-do-not-track")
options.add_argument("--disable-popup-blocking")

options.binary_location = '/snap/bin/chromium'

service = Service('/usr/bin/chromedriver')

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")

time.sleep(2)

title = driver.title
print("Title of the page:", title)

driver.quit()