from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "thatpythonguy2374@gmail.com"
TWITTER_PASSWORD = "Apinder@2374"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        
        button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        button.click()

        time.sleep(40)

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    def tweet_at_provider(self):
        self.driver.get("https://x.com/")

        time.sleep(3)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a')
        login_button.click()

        time.sleep(2)
    
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username.send_keys("thatpythonguy22", Keys.ENTER) 
        
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys("Apinder@2374", Keys.ENTER)

        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div')
        post.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} down / {self.up} up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?")
        time.sleep(2)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()





