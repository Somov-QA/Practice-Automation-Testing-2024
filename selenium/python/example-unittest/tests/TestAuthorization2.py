import unittest

from selenium import webdriver
from support.PageObjects.CommonPage import CommonPage
from support.StepObjects.CommonSteps import CommonSteps

class TestAuthorization2(unittest.TestCase):
    def test(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        tester = CommonSteps(self.driver)
        tester.driver.get('https://somovstudio.github.io/test_eng.html')
        tester.sendForm('admin', '0000')
        text = CommonPage.getResultText(tester.driver)
        self.assertEqual(text, 'Authorization was successful')
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
