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