import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

print("Izvelēties ziņas kategoriju:\n1. Basketbols\n2. Datorspēles\n3. Mode")

choice = int(input("Ievadiet kategorijas numuru: "))

if choice == 1: 
    url = "https://www.sportazinas.com/"
    driver.get(url)
    driver.set_window_size(1920,1080)
    time.sleep(1)
    
    cookies = driver.find_element(By.CSS_SELECTOR , ".stpd_submit_btn.stpd_cta_btn")
    cookies.click()
    time.sleep(1)

    button = driver.find_element(By.CSS_SELECTOR, ".icon.icon-search")
    button.click()

    text = driver.find_element(By.ID, "search")
    text.send_keys("basketbols")

    search = driver.find_element(By.CLASS_NAME, "button")
    search.click()
    time.sleep(6)

    ad = driver.find_element(By.ID, "notify-cancel-button")
    ad.click()
    
elif choice == 2:
    url = "https://www.tvnet.lv/"
    driver.get(url)
    driver.set_window_size(1920,1080)
    time.sleep(3)

    cookies = driver.find_element(By.CLASS_NAME, "css-47sehv")
    cookies.click()

    button = driver.find_element(By.CLASS_NAME, "header-actions-bubble")
    button.click()

    text = driver.find_element(By.CLASS_NAME,"input-element")
    text.send_keys("ceļš un likums")

    search = driver.find_element(By.CLASS_NAME,"input-sumbit")
    search.click()

elif choice == 3:
    url = "https://jauns.lv/"
    driver.get(url)
    driver.set_window_size(1920,1080)
    time.sleep(1)

    cookies = driver.find_element(By.CLASS_NAME, "css-47sehv")
    cookies.click()

    text = driver.find_element(By.CLASS_NAME, "search-shortcut__input")
    text.send_keys("mode")

    button = driver.find_element(By.CLASS_NAME, "search-shortcut__button")
    button.click()
    time.sleep(1)

    ad = driver.find_element(By.CSS_SELECTOR, ".skip-intro.js-intro-skip")
    ad.click()

else:
    print("Nepareizs numurs")

input()