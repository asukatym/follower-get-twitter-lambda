from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import sys
import datetime
import time
from dotenv import load_dotenv
load_dotenv()

import os
def handler(event, context):
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    driver = webdriver.Chrome(options=options, executable_path="/opt/chromedriver")
    driver.get("https://twitter.com/kaoru_mitoma")
    time.sleep(10)
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span")
    follower = element.text
    print(follower)
    

## send to LINE
    message = 'フォロワー数:' + follower
    send_line_notify(message) 
    driver.quit()
    return {
    "statusCode": 200,
    "body": 'hello',
    }

def send_line_notify(notification_message):
        line_notify_token = os.getenv('TOKEN')
        print(line_notify_token)
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'message: {notification_message}'}
        requests.post(line_notify_api, headers = headers, data = data)
