package tests;

import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.Objects;

public class TestAuthorization {
    public static WebDriver driver;

    @BeforeTest
    public static void before(){
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @Test
    public void testAuthorization(){
        driver.get("https://somovstudio.github.io/test_eng.html");
        driver.findElement(By.name("login")).sendKeys("admin");
        driver.findElement(By.name("pass")).sendKeys("0000");
        driver.findElement(By.id("buttonLogin")).click();

        WebElement element = driver.findElement(By.id("result"));
        Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(5));
        wait.until(d -> element.isDisplayed());

        String text = driver.findElement(By.id("textarea")).getAttribute("value");
        System.out.println(text);
        Assert.assertEquals(text, "Authorization was successful");
    }

    @AfterTest
    public static void after(){
        driver.close();
        driver.quit();
    }
}
