package tests;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import org.openqa.selenium.chrome.ChromeDriver;

import support.PageObjects.CommonPage;
import support.StepObjects.CommonSteps;
import support.Helper;

public class TestAuthorization2 {

    public static CommonSteps tester;

    @BeforeAll
    public static void before(){
        tester = new CommonSteps(new ChromeDriver());
        tester.driver.manage().window().maximize();
    }

    @Tag("PROD")
    @Test
    public void testAuthorization(){
        tester.driver.get(Helper.URL);
        tester.sendForm(Helper.LOGIN, Helper.PASSWORD);
        String text = CommonPage.getResultText(tester.driver);
        Assertions.assertEquals(text, "Authorization was successful");
    }

    @AfterAll
    public static void after(){
        tester.driver.close();
        tester.driver.quit();
    }
}
