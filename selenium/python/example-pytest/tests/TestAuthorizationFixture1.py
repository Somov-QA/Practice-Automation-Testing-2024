import pytest

from selenium import webdriver
from support.PageObjects.CommonPage import CommonPage
from support.StepObjects.CommonSteps import CommonSteps

@pytest.fixture(scope="function")
def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test(init_driver):
    tester = CommonSteps(init_driver)
    tester.driver.get('https://somovstudio.github.io/test_eng.html')
    tester.sendForm( 'admin', '0000')
    text = CommonPage.getResultText(tester.driver)
    assert text == 'Authorization was successful', "Получено некорректное сообщение"
    tester.driver.close()
    tester.driver.quit()