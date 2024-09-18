# Selenium (Javascript)

Автоматизированное тестирование Selenium на языке JavaScript

<p>
	<h4>Ссылки на ресурсы:</h2>
	Официальное описание <a href="https://www.selenium.dev/selenium/docs/api/javascript/index.html">Selenium WebDriver JavaScript API</a><br>
	Страница приложения <a href="https://nodejs.org/">NodeJS</a><br>
</p>

<p>
	<h4>Создание проекта и запуск автотеста:</h2>
	<ul>
		<li>Скачать и установить <a href="https://code.visualstudio.com/">Visual Studio Code</a></li>
		<li>Скачать и установить <a href="https://nodejs.org/en/download/prebuilt-installer">NodeJS</a></li>
		<li>Открыть консоль и проверить работу NodeJS с помощью команты
			<pre><code>
npm version
			</code></pre>
		</li>
		<li>Создать папку проекта и выполнить в консоли команду
			<pre><code>
npm install selenium-webdriver
			</code></pre>
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/images/install_selenium_webdriver_javascript.jpg">
			</p>
		</li>
		<li>Открыть проект в редакторе Visual Studio Code</li>
		<li>Создать файл test1.js и описать автотест следующим образом
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
node test1.js
			</code></pre>
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/images/test1.jpg">
			</p>
			<p align="center">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/images/console_test1.jpg">
			</p>
		</li>
	</ul>
</p>
