from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium_stealth import stealth
import random
import undetected_chromedriver as uc
import time

options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = uc.Chrome(use_subprocess=True, headless=False)



timers = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
variables = [
    "https://www.tiktok.com/login/phone-or-email/email", "//input[@placeholder='Email or username']",
    "//input[@placeholder='Password']", "//button[@type='submit']"
]

with open('user.txt') as f:
    line = f.readlines()
username = line[0][10:-1]
password = line[1][10:-1 ]

start_b = time.time()
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

def logging_in():
        driver.get(variables[0])

        try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, variables[1])))
                fieldForm = driver.find_element("xpath", variables[1])
        except:
                driver.quit()
        finally:
                for i in username:
                        fieldForm.send_keys(i)
                        time.sleep(float("0." + random.choice(timers[0:3]) + random.choice(timers[0:4]) + random.choice(timers[0:9])))

        fieldForm = driver.find_element("xpath", variables[2])
        for i in password:
                fieldForm.send_keys(i)
                time.sleep(float("0." + random.choice(timers[0:3]) + random.choice(timers[0:4]) + random.choice(timers[0:9])))

        try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, variables[3])))
        except:
                driver.quit()
        finally:
                button = driver.find_element("xpath", variables[3])
                button.click()

logging_in()
end = time.time()
print(f"You has been succesfully logged in to your tik tok account, script executed in {end-start_b}s")
