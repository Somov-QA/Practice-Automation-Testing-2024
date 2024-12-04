# Selenium (Javascript)

Автоматизированное тестирование Selenium на языке JavaScript

<p>
	<h4>Содержание:</h2>
	<ul>
		<li>example-simple</li>
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
		<li>Документация <a href="https://www.selenium.dev/selenium/docs/api/javascript/index.html">API Docs (javascript)</a></li>
		<li>Официальная страница <a href="https://code.visualstudio.com/">Visual Studio Code</a></li>
		<li>Официальная страница <a href="https://nodejs.org/">NodeJS</a></li>
	</ul>
</p>

<p>
	<h4>Создание проекта и запуск простого автотеста:</h4>
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
		</li>
		<li>Результат автотеста в консоли
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/javascript_example_simple_test.jpg">
			</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/javascript_console_example_simple_test.jpg">
			</p>
		</li>
	</ol>
</p>

<hr>

<p>
	<h2>Описание паттернов PageObjects и StepObjects</h2>
	<p>Создать папку support со следующей структурой:</p>
	<p>Файл Helper.js - описаны константы
		<pre><code>
module.exports = class Helper {
    static URL = "https://somovstudio.github.io/test_eng.html";
    static LOGIN = "admin";
    static PASSWORD = "0000";
}
		</code></pre>
	</p>
	<p>Файл CommonPage.js - описаны локаторы и статичные методы
		<pre><code>
const { Builder, Browser, By, Key, until } = require('selenium-webdriver');

module.exports = class CommonPage {
    static nameLogin = "login";
    static namePassword = "pass";
    static idButtonLogin = "buttonLogin";
    static idResult = "result";
    static idTextarea = "textarea";

    static async getResultText(driver) {
        let element = await driver.findElement(By.id('result'));
        await driver.wait(until.elementIsVisible(element), 5000);
        let text = await driver.findElement(By.id('textarea')).getAttribute('value');
        return text;
    }
}; 
		</code></pre>
	</p>
	<p>Файл CommonSteps.js - описан класс методов для выполнения действий
		<pre><code>
const { Builder, Browser, By, Key, until } = require('selenium-webdriver');

module.exports = class CommonSteps {
    constructor(webdriver) {
        this.driver = webdriver;
    }

    async sendFormAsync(login, password) {
        await this.driver.findElement(By.name('login')).sendKeys('admin');
        await this.driver.findElement(By.name('pass')).sendKeys('0000');
        await this.driver.findElement(By.id('buttonLogin')).click();
    }
}; 
		</code></pre>
	</p>
	<p>Файл автотеста testAuthorization.js описать следующим образом
		<pre><code>
var Helper = require('./support/Helper');
var CommonPage = require('./support/PageObjects/CommonPage');
var CommonSteps = require('./support/StepObjects/CommonSteps');

const { Builder, Browser, By, Key, until } = require('selenium-webdriver');
		</code></pre>
		<pre><code>
(async function TestAuthorization() {
    let driver = await new Builder().forBrowser(Browser.CHROME).build();
    let tester = new CommonSteps(driver);
    try {
        await driver.get(Helper.URL);
        await tester.sendFormAsync(Helper.LOGIN, Helper.PASSWORD);
        let text = await CommonPage.getResultText(tester.driver);
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
	</p>
	<p align="left">
		<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/javascript_patterns.jpg">
	</p>
	<p>Запуск автотест командой
		<pre><code>
node testAuthorization.js
		</code></pre>
	</p>
</p>