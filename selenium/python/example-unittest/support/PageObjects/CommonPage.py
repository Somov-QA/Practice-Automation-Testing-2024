from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CommonPage:
    nameLogin = "login"
    namePassword = "pass"
    idButtonLogin = "buttonLogin"
    idResult = "result"
    idTextarea = "textarea"

    def getResultText(driver):
        element = driver.find_element(By.ID, CommonPage.idResult)
        wait = WebDriverWait(driver, timeout=5)
        wait.until(lambda d: element.is_displayed())
        text = driver.find_element(By.ID, CommonPage.idTextarea).get_property('value')
        print("Get message: " + text)
        return text