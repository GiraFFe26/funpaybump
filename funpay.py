from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from random import randint


def bumping(user_link):
    delay = 10
    login = 'login'
    password = 'password'
    service = Service()
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('https://funpay.com/account/login')
    try:
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.NAME, 'login')))
    except TimeoutException:
        time.sleep(delay)
    driver.find_element(By.NAME, 'login').send_keys(login)
    try:
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.NAME, 'login')))
    except TimeoutException:
        time.sleep(delay)
    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(20)
    while True:
        driver.get(user_link)
        try:
            WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.CLASS_NAME, 'offer-list-title')))
        except TimeoutException:
            time.sleep(delay)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        buttons = soup.find_all('a', class_='btn btn-default btn-plus')
        for button in buttons:
            url = button.get('href')
            driver.get(url)
            try:
                WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/button')))
            except TimeoutException:
                time.sleep(delay)
            driver.find_element(By.XPATH, '/html/body/div/div[1]/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/button').click()
            time.sleep(1)
            try:
                timer = driver.find_element(By.ID, "site-message").text
                print(f'{timer} - {driver.find_element(By.CLASS_NAME, "inside").text}')
            except NoSuchElementException:
                print(f'Объявление было поднято - {driver.find_element(By.CLASS_NAME, "inside").text}')
        time.sleep(randint(1200, 1800))


def main():
    bumping('user_link')


if __name__ == '__main__':
    main()
