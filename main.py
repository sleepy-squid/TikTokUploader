from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import argparse
import os
import time

class TikTokUploader:
    def __init__(self):
        path = Service(r"C:\Users\Denver Whiteley\Documents\PythonProjects\TikTokUploader\chromedrivernew.exe")
        self.driver = webdriver.Chrome(service=path)
        self.executor_url = self.driver.command_executor._url
        self.session_id = self.driver.session_id
        stealth(self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
        self.username = "subredditreadings"
        self.password = "*321Cheeseburger123*"
        self.videoloc = r"C:\Users\Denver Whiteley\Documents\PythonProjects\RedditVideoMakerBot\assets\final_video.mp4"

    def upload(self, viewSetting, videoPath, caption):
        #opens browser to tiktok homepage
        #self.driver.get("https://tiktok.com")
        #time.sleep(1)
        #navigates to the login page
        self.driver.get("https://www.tiktok.com/login/phone-or-email/email")
        time.sleep(2)
        #filling in the login form
        userfield = self.driver.find_element(By.CSS_SELECTOR,"#loginContainer > div.tiktok-xabtqf-DivLoginContainer.exd0a430 > form > div.tiktok-11aoaap-DivInputContainer.e93gz7m0 > input")
        userfield.click()
        userfield.send_keys(self.username)
        time.sleep(2)
        passfield = self.driver.find_element(By.CSS_SELECTOR, "#loginContainer > div.tiktok-xabtqf-DivLoginContainer.exd0a430 > form > div.tiktok-15iauzg-DivContainer.ewblsjs0 > div > input")
        passfield.click()
        passfield.send_keys(self.password)
        time.sleep(0.5)
        loginbutton = self.driver.find_element(By.CSS_SELECTOR, "#loginContainer > div.tiktok-xabtqf-DivLoginContainer.exd0a430 > form > button")
        loginbutton.click();
        time.sleep(3)
        #going to the upload video page
        self.driver.get("https://www.tiktok.com/upload?lang=en")
        time.sleep(2)
        #adding the file
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div > div > div > div > div.jsx-410242825.contents-v2 > div.jsx-410242825.uploader > div > input"))).send_keys(videoloc)
        #filebutton = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/div')
        #filebutton.send_keys(videoloc)
        time.sleep(60)

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
