# Practice-Automation-Testing-2024

[![License](http://img.shields.io/:license-mit-blue.svg)](https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/LICENSE)

Практика автоматизированного тестирования 2024

<p>
	<h4>Содержание практики:</h2>
	<ul>
		<li>автотесты Selenium (Java)</li>
		<li>автотесты Selenuim (Python)</li>
		<li>автотесты Selenuim (JavaScript)</li>
	</ul>
</p>
<p>
	<h4>Ссылки на ресурсы:</h2>
	<ul>
		<li>Официальный сайт Selenuim: <a href="https://www.selenium.dev/">https://www.selenium.dev/</a></li>
		<li>Документация <a href="https://www.selenium.dev/documentation/overview/">https://www.selenium.dev/documentation/overview/</a></li>
		<li>Быстрый старт <a href="https://www.selenium.dev/documentation/grid/getting_started/">https://www.selenium.dev/documentation/grid/getting_started/</a></li>
		<li>Скачать Selenium Server (Grid): <a href="https://www.selenium.dev/downloads/">https://www.selenium.dev/downloads/</a></li>
		<li>Chrome драйвер <a href="https://googlechromelabs.github.io/chrome-for-testing/#stable">https://googlechromelabs.github.io/chrome-for-testing/#stable</a></li>
	</ul>
</p>
<p>
	<h4>Установка и запуск Selenium Grid:</h2>
	<ul>
		<li>Скачать и установить <a href="https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html">Java SE Development Kit 11</a></li>
		<li>Скачать и установить браузер <a href="https://www.google.com/intl/ru/chrome/browser-tools/">Chrome</a></li>
		<li>Скачать драйвер <a href="https://googlechromelabs.github.io/chrome-for-testing/#stable">ChromeDriver</a></li>
		<li>Скачать jar файл <a href="https://www.selenium.dev/downloads/">Selenium Server</a> или с <a href="https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.24.0">github</a></li>
		<li>Создать папку C:\selenium\ в которую скопировать файлы: <b>selenium-server-4.24.0.jar</b>, <b>chromedriver.exe</b></li>
		<li>В переменной Path прописать путь к папке C:\selenium
			<br>(Панель управления > Система > Доплнительные параметры системы > Переменные среды)
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/images/path.jpg">
			</p>
		</li>
		<li>В папке C:\selenium\ создать файл <b>run-selenium.bat</b> в котором написать:
			<pre><code>
cd C:\selenium
java -jar selenium-server-4.24.0.jar standalone
			</code></pre>
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/images/folder.jpg">
			</p>
		</li>
		<li>Запустить файл run-selenium.bat
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/images/console.jpg">
			</p>
		</li>
		<li>Чтобы остановить Selenium нажмите в консоли Ctrl+C и затем Y</li>
	</ul>
</p>
