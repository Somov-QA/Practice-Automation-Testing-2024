package support.PageObjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class CommonPage {
    public static String nameLogin = "login";
    public static String namePassword  = "pass";
    public static String idButtonLogin  = "buttonLogin";
    public static String idResult  = "result";
    public static String idTextarea  = "textarea";

    public static String getResultText(WebDriver driver){
        WebElement element = driver.findElement(By.id(CommonPage.idResult));
        Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(5));
        wait.until(d -> element.isDisplayed());
        String text = driver.findElement(By.id(CommonPage.idTextarea)).getAttribute("value");
        System.out.println("Get message: " + text);
        return text;
    }
}

