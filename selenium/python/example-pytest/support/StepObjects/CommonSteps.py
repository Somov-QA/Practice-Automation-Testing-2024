from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from support.PageObjects.CommonPage import CommonPage

class CommonSteps:

    def __init__(self, webdriver):
        self.driver = webdriver

    def sendForm(self, login, password):
        self.driver.find_element(By.NAME, CommonPage.nameLogin).send_keys(login)
        self.driver.find_element(By.NAME, CommonPage.namePassword).send_keys(password)
        self.driver.find_element(By.ID, CommonPage.idButtonLogin).click()
