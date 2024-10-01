# Selenium (Python)

Автоматизированное тестирование Selenium на языке Python

<p>
	<h4>Содержание:</h2>
	<ul>
		<li>example-simple</li>
		<li>example-Unittest</li>
		<li>example-PyTest</li>
		<li>demo</li>
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
	<h4>Создание проекта и запуск автотеста:</h2>
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
		<li>Создать пакет tests и в нём файл unit test с именем test1
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_create_test.jpg">
			</p>
		</li>
		<li>В файле test1.py описать автотест следующим образом
			<pre><code>
driver = webdriver.Chrome()
driver.get('https://somovstudio.github.io/test_eng.html')
driver.find_element(By.NAME, 'login').send_keys('admin')
driver.find_element(By.NAME, 'pass').send_keys('0000')
driver.find_element(By.ID, 'buttonLogin').click()
element = driver.find_element(By.ID, 'result')
wait = WebDriverWait(driver, timeout=5)
wait.until(lambda d: element.is_displayed())
text = driver.find_element(By.ID, 'textarea').get_attribute('value')
print("TEXT: " + text)
self.assertEqual(text, 'Authorization was successful')
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_test1.jpg">
			</p>
		</li>
		<li>Запуск автотеста в редакторе PyCharm
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_test1_run.jpg">
			</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_test1_result.jpg">
			</p>
		</li>
		<li>Запуск автотеста из консоли
			<pre><code>
python E:\Git\SomovQA\Practice-Automation-Testing-2024\selenium\python\Autotesting\tests\test1.py
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/python_console_run.jpg">
			</p>
		</li>
	</ol>
</p>