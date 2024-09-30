# Selenium (Javascript)

Автоматизированное тестирование Selenium на языке JavaScript

<p>
	<h4>Содержание:</h2>
	<ul>
		<li>example-simple</li>
		<li>example-demo</li>
	</ul>
</p>

<p>
	<h4>Полезные ссылки:</h2>
	<ul>
		<li>Официальная документация <a href="https://www.selenium.dev/documentation/">The Selenium Browser Automation Project</a></li>
		<li>Документация <a href="https://www.selenium.dev/selenium/docs/api/javascript/index.html">API Docs</a></li>
		<li>Официальная страница <a href="https://code.visualstudio.com/">Visual Studio Code</a></li>
		<li>Официальная страница <a href="https://nodejs.org/">NodeJS</a></li>
	</ul>
</p>

<p>
	<h4>Создание проекта и запуск простого автотеста:</h2>
	<ol>
		<li>Скачать и установить <a href="https://code.visualstudio.com/">Visual Studio Code</a></li>
		<li>Скачать и установить <a href="https://nodejs.org/en/download/prebuilt-installer">NodeJS</a></li>
		<li>Открыть консоль и проверить работу NodeJS с помощью команты
			<pre><code>
npm -v
			</code></pre>
		</li>
		<li>Создать папку проекта example-simple и в корне этой папки выполнить в консоли команду:
			<pre><code>
npm install selenium-webdriver
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/javascript_install_selenium_webdriver.jpg">
			</p>
		</li>
		<li>Открыть папку в редакторе Visual Studio Code</li>
		<li>Создать файл test.js и описать автотест следующим образом
			<pre><code>
const { Builder, Browser, By, Key, until } = require('selenium-webdriver');

(async function example() {
    let driver = await new Builder().forBrowser(Browser.CHROME).build();
    try {
        await driver.get('https://somovstudio.github.io/test_eng.html');
        await driver.findElement(By.name('login')).sendKeys('admin');
        await driver.findElement(By.name('pass')).sendKeys('0000');
        await driver.findElement(By.id('buttonLogin')).click();
        let element = await driver.findElement(By.id('result'));
        await driver.wait(until.elementIsVisible(element), 5000);
        let text = await driver.findElement(By.id('textarea')).getAttribute('value');
        if (text == 'Authorization was successful'){
            console.log('Test - SUCCESS');
        }else{
            throw new Error('Test - FAILED');
        }
    } finally {
        await driver.quit();
    }
})()
			</code></pre>
		</li>
		<li>Запустить автотест командой
			<pre><code>
node test.js
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/javascript_example_simple_test.jpg">
			</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/javascript_console_example_simple_test.jpg">
			</p>
		</li>
	</ol>
</p>
