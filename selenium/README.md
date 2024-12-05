# Selenium

<p>
	<h4>Содержание:</h2>
	<ul>
		<li><a href="https://github.com/Somov-QA/Practice-Automation-Testing-2024/tree/main/selenium/java">java</a></li>
		<li><a href="https://github.com/Somov-QA/Practice-Automation-Testing-2024/tree/main/selenium/javascript">javascript</a></li>
		<li><a href="https://github.com/Somov-QA/Practice-Automation-Testing-2024/tree/main/selenium/python">python</a></li>
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
		<li>Скачать Selenium Server (Grid): <a href="https://www.selenium.dev/downloads/">https://www.selenium.dev/downloads/</a></li>
		<li>Chrome драйвер <a href="https://googlechromelabs.github.io/chrome-for-testing/#stable">https://googlechromelabs.github.io/chrome-for-testing/#stable</a></li>
	</ul>
</p>
<p>
	<h4>Установка и запуск Selenium Grid:</h2>
	<ol>
		<li>Скачать и установить <a href="https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html">Java SE Development Kit 11</a></li>
		<li>Скачать и установить браузер <a href="https://www.google.com/intl/ru/chrome/browser-tools/">Chrome</a></li>
		<li>Скачать драйвер <a href="https://googlechromelabs.github.io/chrome-for-testing/#stable">ChromeDriver</a></li>
		<li>Скачать jar файл <a href="https://www.selenium.dev/downloads/">Selenium Server</a> или с <a href="https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.24.0">github</a></li>
		<li>Создать папку C:\selenium\ в которую скопировать файлы: <b>selenium-server-4.24.0.jar</b>, <b>chromedriver.exe</b></li>
		<li>В переменной Path прописать путь к папке C:\selenium
			<br>(Панель управления > Система > Доплнительные параметры системы > Переменные среды)
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/path.jpg">
			</p>
		</li>
		<li>В папке C:\selenium\ создать файл <b>run-selenium.bat</b> в котором написать:
			<pre><code>
cd C:\selenium
java -jar selenium-server-4.24.0.jar standalone
			</code></pre>
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/folder.jpg">
			</p>
		</li>
		<li>Запустить файл run-selenium.bat
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/console.jpg">
			</p>
		</li>
		<li>Чтобы остановить Selenium нажмите в консоли Ctrl+C и затем Y</li>
	</ol>
</p>
