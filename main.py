from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import argparse
import os
import time

class TikTokUploader:
    def __init__(self):
        path = Service(r"C:\Users\Denver Whiteley\Documents\PythonProjects\TikTokUploader\chromedriver.exe")
        self.driver = webdriver.Chrome(service=path)
        self.executor_url = self.driver.command_executor._url
        self.session_id = self.driver.session_id

    def upload(self, viewSetting, videoPath, caption):
        #opens browser to tiktok homepage
        self.driver.get('https://tiktok.com')
        #navigates to the login page
        self.driver.get("https://www.tiktok.com/login/phone-or-email/email")
        #filling in the login form
        

def main():
    parser = argparse.ArgumentParser(description='This bot allows you to upload a TikTok video automatically')
    parser.add_argument("--privacy", choices=['Private', 'Friends only', 'Public'], help="Private, Friends only, or Public", required=True)
    parser.add_argument("--videoPath", help="Absolute path to video, i.e. /Users/username/Downloads/IMG_1648.MOV", required=True)
    parser.add_argument("--caption", help="Enter a caption, i.e. Uploaded by a bot #bot #cs #cool", required=True)
    args = parser.parse_args()
    bot = TikTokUploader()
    bot.upload(viewSetting=args.privacy, videoPath=args.videoPath, caption=args.caption)

if __name__ == '__main__':
    main()
