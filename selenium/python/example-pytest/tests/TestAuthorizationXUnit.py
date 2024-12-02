import pytest

from selenium import webdriver
from support.PageObjects.CommonPage import CommonPage
from support.StepObjects.CommonSteps import CommonSteps

class TestAuthorizationXUnit:
    driver = 0

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        self.driver.get('https://somovstudio.github.io/test_eng.html')
        tester = CommonSteps(self.driver)
        CommonSteps.sendForm(tester, 'admin', '0000')
        text = CommonPage.getResultText(self.driver)
        assert text == 'Authorization was successful', "Получено некорректное сообщение"

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["-s", "TestAuthorizationXUnit.py"])