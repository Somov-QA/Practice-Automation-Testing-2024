package support.StepObjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;
import support.PageObjects.CommonPage;

public class CommonSteps {
    public final WebDriver driver;

    public CommonSteps(WebDriver webdriver){
        driver = webdriver;
    }

    public void sendForm(String login, String password){
        driver.findElement(By.name(CommonPage.nameLogin)).sendKeys(login);
        driver.findElement(By.name(CommonPage.namePassword)).sendKeys(password);
        driver.findElement(By.id(CommonPage.idButtonLogin)).click();
    }

}
