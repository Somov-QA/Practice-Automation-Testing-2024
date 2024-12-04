var Helper = require('./support/Helper');
var CommonPage = require('./support/PageObjects/CommonPage');
var CommonSteps = require('./support/StepObjects/CommonSteps');

const { Builder, Browser, By, Key, until } = require('selenium-webdriver');

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