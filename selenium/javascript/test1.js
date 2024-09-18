const { Builder, Browser, By, Key, until } = require('selenium-webdriver');

(async function example() {
    let driver = await new Builder().forBrowser(Browser.CHROME).build();
    try {
        await driver.get('https://somovstudio.github.io/test.html');
        await driver.findElement(By.name('login')).sendKeys('admin');
        await driver.findElement(By.name('pass')).sendKeys('0000');
        await driver.findElement(By.id('buttonLogin')).click();
        let element = await driver.findElement(By.id('result'));
        await driver.wait(until.elementIsVisible(element), 5000);
        let text = await driver.findElement(By.id('textarea')).getAttribute('value');
        if (text == 'Вы успешно авторизованы'){
            console.log('Test - SUCCESS');
        }else{
            throw new Error('Test - FAILED');
        }
    } finally {
        await driver.quit();
    }
})()