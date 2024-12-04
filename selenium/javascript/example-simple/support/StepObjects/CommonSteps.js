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