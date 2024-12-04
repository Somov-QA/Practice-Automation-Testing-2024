# Selenium (Python)

Автоматизированное тестирование Selenium на языке Python

<p>
	<h4>Содержание:</h2>
	<ul>
		<li>example-simple</li>
		<li>example-unittest</li>
		<li>example-pytest</li>
	</ul>
</p>

<p>
	<h4>Документация:</h2>
	<ul>
		<li>Подное описание практики в <a href="https://github.com/Somov-QA/Practice-Automation-Testing-2024/tree/main/_docs">документе</a></li>
		<li>Тест-кейсы для автотестов описаны в <a href="https://github.com/Somov-QA/Practice-Automation-Testing-2024/tree/main/_test-cases">документе</a></li>
	</ul>
</p>

<p>
	<h4>Полезные ссылки:</h2>
	<ul>
		<li>Официальная документация <a href="https://www.selenium.dev/documentation/">The Selenium Browser Automation Project</a></li>
		<li>Документация <a href="https://www.selenium.dev/selenium/docs/api/py/index.html">API Docs (python)</a></li>
		<li>Официальная страница <a href="https://www.jetbrains.com/pycharm/download/other.html">PyCharm Community Edition</a></li>
		<li>Официальная страница <a href="https://www.python.org/">Python</a></li>
	</ul>
</p>

<p>
	<h4>Создание проекта и запуск простого автотеста:</h4>
	<ol>
		<li>Скачать и установить <a href="https://www.python.org/">Python</a></li>
		<li>В переменной Path прописать путь к папке C:\Program Files\Python
			<br>(Панель управления > Система > Доплнительные параметры системы > Переменные среды)
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_path.jpg">
			</p>
		</li>
		<li>Проверить версию Python, посмотреть установленные библиотеки, обновить pip
			<pre><code>
python -V
pip list
python -m pip install --upgrade pip
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_version_console.jpg">
			</p>
		</li>
		<li>Установить Selenium командой
			<pre><code>
pip install -U selenium
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_install.jpg">
			</p>
		</li>
		<li>Проверить установленную версию Selenium
			<pre><code>
pip list
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_pip_list_selenium.jpg">
			</p>
		</li>
		<li>Скачать и установить <a href="https://www.jetbrains.com/pycharm/download/other.html">PyCharm Community Edition</a></li>
		<li>В редакторе PyCharm создаем новый проект
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_new_project.jpg">
			</p>
		</li>
		<li>Настройки проекта
			<br> Добавить пакет Selenium
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_project_settings_add_pack.jpg">
			</p>
			<br> При установке будут добавлены следующие пакеты
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_project_settings_selenium.jpg">
			</p>
		</li>
		<li>В файле main.py описать автотест следующим образом
			<pre><code>
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
	text = driver.find_element(By.ID, 'textarea').get_property('value')
	if text == 'Authorization was successful':
		print("Test - SUCCESS")
	else:
		print("Test - FAILED")
		raise Exception('Test - FAILED')
	driver.close()
	driver.quit()

if __name__ == '__main__':
	main()
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_main.jpg">
			</p>
		</li>
		<li>Запуск автотеста в редакторе PyCharm
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_main_run.jpg">
			</p>
		</li>
		<li>Запуск автотеста из консоли
			<pre><code>
python E:\Git\SomovQA\Practice-Automation-Testing-2024\selenium\python\examplesimple\main.py
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_main_console_run.jpg">
			</p>
		</li>
	</ol>
</p>
<hr>
<p>
	<h2>Практика применения Unittest</h2>
	<p>Создать пакет с именем tests</p>
	<p>В пакете tests создать модульный тест (Python unit test) с именем TestAuthorization.py</p>
	<p align="left">
		<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_create_unit_test.jpg">
	</p>
	<p>В файле TestAuthorization.py описать автотест следующим образом
		<pre><code>
import unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://somovstudio.github.io/test_eng.html')
        driver.find_element(By.NAME, 'login').send_keys('admin')
        driver.find_element(By.NAME, 'pass').send_keys('0000')
        driver.find_element(By.ID, 'buttonLogin').click()
        element = driver.find_element(By.ID, 'result')
        wait = WebDriverWait(driver, timeout=5)
        wait.until(lambda d: element.is_displayed())
        text = driver.find_element(By.ID, 'textarea').get_property('value')
        print("Get message: " + text)
        self.assertEqual(text, 'Authorization was successful')
        driver.close()
        driver.quit()

if __name__ == '__main__':
    unittest.main()
		</code></pre>
	</p>
	<p>Запуск автотеста в редакторе PyCharm или в консоли командой:
		<pre><code>
python E:\Git\SomovQA\Practice-Automation-Testing-2024\selenium\python\example-unittest\tests\TestAuthorization.py
		</code></pre>
	</p>
</p>
<hr>
<p>
	<h2>Практика применения PyTest</h2>
	<p>Установить PyTest
		<pre><code>
pip install pytest
pip3 install pytest
		</code></pre>
	</p>
	<p>Для проверки выполнить команду
		<pre><code>
pip3 show pytest
pytest --version
		</code></pre>
	</p>
	<p>В корне проекта создать пакет с именем tests</p>
	<p>В пакете tests создать файл (Python file) с именем TestAuthorization.py</p>
	<p>В файле TestAuthorization.py описать автотест следующим образом
		<pre><code>
import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

def test_authorization():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://somovstudio.github.io/test_eng.html')
    driver.find_element(By.NAME, 'login').send_keys('admin')
    driver.find_element(By.NAME, 'pass').send_keys('0000')
    driver.find_element(By.ID, 'buttonLogin').click()
    element = driver.find_element(By.ID, 'result')
    wait = WebDriverWait(driver, timeout=5)
    wait.until(lambda d: element.is_displayed())
    text = driver.find_element(By.ID, 'textarea').get_property('value')
    print("Get message: " + text)
    assert text == 'Authorization was successful', "Получено некорректное сообщение"
    driver.close()
    driver.quit()

if __name__ == '__main__':
    pytest.main(["-s", "TestAuthorization.py"])
		</code></pre>
	</p>
	<p>После установки pytest.exe будет находдится по адресу \example-pytest\.venv\Scripts</p>
	<p align="left">
		<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_pytest_exe.jpg">
	</p>
	<p>Запуск автотеста через консоль
		<pre><code>
E:
cd E:\Git\SomovQA\Practice-Automation-Testing-2024\selenium\python\example-pytest\.venv\Scripts
pytest -s -v E:\Git\SomovQA\Practice-Automation-Testing-2024\selenium\python\example-pytest\tests\TestAuthorization.py
		</code></pre>
	</p>
	<p align="left">
		<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_pytest_run.jpg">
	</p>
</p>
<hr>
<p>
	<h2>Практика PyTest в стиле xUnit</h2>
	<p>Описание паттернов PageObjects и StepObjects</p>
	<p align="left">
		<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_patterns.jpg">
	</p>
	<p>Файл CommonPage.py - описаны локаторы и статичные методы
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
        text = driver.find_element(By.ID, 
                     CommonPage.idTextarea).get_property('value')
        print("Get message: " + text)
        return text
	</p>
	<br>
	<p>Файл CommonSteps.py - описан класс методов для выполнения действий
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
        self.driver.find_element(By.NAME, 
                     CommonPage.nameLogin).send_keys(login)
        self.driver.find_element(By.NAME, 
                     CommonPage.namePassword).send_keys(password)
        self.driver.find_element(By.ID, 
                     CommonPage.idButtonLogin).click()
	</p>
	<br>
	<p>Файл автотеста TestAuthorizationXUnit.py - используются ранее описанные паттерны
import pytest
from selenium import webdriver
from support.PageObjects.CommonPage import CommonPage
from support.StepObjects.CommonSteps import CommonSteps

class TestAuthorizationXUnit:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test(self):
        tester = CommonSteps(self.driver)
        tester.driver.get('https://somovstudio.github.io/test_eng.html')
        tester.sendForm( 'admin', '0000')
        text = CommonPage.getResultText(tester.driver)
        assert text == 'Authorization was successful', "Получено некорректное сообщение"

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(["-s", "TestAuthorizationXUnit.py"])
	</p>
</p>
<hr>
<p>
	<h2>Практика PyTest с применением Fixture</h2>
	<p>
		<pre><code>
		</code></pre>
	</p>
</p>