from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

def main():
    driver = webdriver.Chrome()
    driver.get('https://somovstudio.github.io/test_eng.html')
    driver.find_element(By.NAME, 'login').send_keys('admin')
    driver.find_element(By.NAME, 'pass').send_keys('0000')
    driver.find_element(By.ID, 'buttonLogin').click()
    element = driver.find_element(By.ID, 'result')
    wait = WebDriverWait(driver, timeout=5)
    wait.until(lambda d: element.is_displayed())
    text = driver.find_element(By.ID, 'textarea').get_attribute('value')
    if text == 'Authorization was successful':
        print("Test - SUCCESS")
    else:
        print("Test - FAILED")
        raise Exception('Test - FAILED')
    driver.close()
    driver.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


