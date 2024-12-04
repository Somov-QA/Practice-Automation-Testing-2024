# Selenium (Java)

Автоматизированное тестирование Selenium на языке Java

<p>
	<h4>Содержание:</h4>
	<ul>
		<li>example-simple</li>
		<li>example-junit</li>
		<li>example-testng</li>
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
	<h4>Полезные ссылки:</h4>
	<ul>
		<li>Официальная документация <a href="https://www.selenium.dev/documentation/">The Selenium Browser Automation Project</a></li>
		<li>Документация <a href="https://www.selenium.dev/documentation/webdriver/getting_started/">Getting started</a></li>
		<li>Документация <a href="https://www.selenium.dev/documentation/webdriver/getting_started/install_library/">Install a Selenium library</a></li>
		<li>Документация <a href="https://www.selenium.dev/selenium/docs/api/java/index.html">API Docs (java)</a></li>
		<li>Официальная страница <a href="https://www.jetbrains.com/idea/download/other.html">IntelliJ IDEA Community Edition</a></li>
		<li>Официальная страница <a href="https://mvnrepository.com/">Maven</a></li>
		<li>Официальная страница <a href="https://junit.org/junit5/">junit5</a></li>
		<li>Официальная страница <a href="https://testng.org/">TestNG</a></li>
	</ul>
</p>

<p>
	<h4>Создание проекта и запуск простого автотеста:</h4>
	<ol>
		<li>Скачать и установить <a href="https://www.jetbrains.com/idea/download/other.html">IntelliJ IDEA Community Edition</a></li>
		<li>Скачать и установить <a href="https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html">Java SE Development Kit 11</a></li>
		<li>В редакторе IntelliJ IDEA создаем новый проект example-simple выбрав Maven и SDK: Oracle OpenJDK 11
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_new_project.jpg">
			</p>
		</li>
		<li>Подключить библиотеку Selenium к проекту в файле pom.xml
		<br> ссылка: <a href="https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java">https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java</a>
			<pre><code>
< dependency >
	< groupId >org.seleniumhq.selenium< /groupId >
	< artifactId >selenium-java< /artifactId >
	< version >4.25.0< /version >
< /dependency >
			</code></pre>
		</li>
		<li>Выполнить загрузку библиотеки в файле pom.xml
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_load_maven_selenium.jpg">
			</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_pom.jpg">
			</p>
		</li>
		<li>В файле Main.java описать автотест следующим образом
			<pre><code>
WebDriver driver = new ChromeDriver();
driver.get("https://somovstudio.github.io/test_eng.html");
driver.findElement(By.name("login")).sendKeys("admin");
driver.findElement(By.name("pass")).sendKeys("0000");
driver.findElement(By.id("buttonLogin")).click();

WebElement element = driver.findElement(By.id("result"));
Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(5));
wait.until(d -> element.isDisplayed());

String text = driver.findElement(By.id("textarea")).getAttribute("value");
if(Objects.equals(text, "Authorization was successful")){
		System.out.println("Test - SUCCESS");
}else{
		throw new Error("Test - FAILED");
}

driver.close();
driver.quit();
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_main.jpg">
			</p>
		</li>
		<li>Запустить автотест нажав кнопку Run в IntelliJ IDEA
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_run.jpg">
			</p>
		</li>
		<li>Результат автотеста в консоли IntelliJ IDEA
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_console.jpg">
			</p>
		</li>
	</ol>
</p>
<hr>
<p>
	<h2>Практика применения JUnit</h2>
	<p>Подключить библиотеку JUnit Jupiter API к проекту в файле pom.xml
		<br> ссылка: <a href="https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-api">https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-api</a>
		<pre><code>
< dependency >
	< groupId >org.junit.jupiter< /groupId >
	< artifactId >junit-jupiter-api< /artifactId >
	< version >5.11.3< /version >
	< scope >test< /scope >
< /dependency >
		</code></pre>
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_pom_junit.jpg">
		</p>
	</p>
	<p>В папке test создать пакет tests
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_create_package.jpg">
		</p>
	</p>
	<p>В пакете tests создать класс автотеста TestAuthorization.java
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_create_test.jpg">
		</p>
	</p>
	<p>Аннотации JUnit 5
		<table>
			<tr>
				<th>Аннотации</th>
				<th>Описание</th>
		   </tr>
		   <tr>
				<td>@BeforeEach</td>
				<td>Аннотированный метод будет запускаться перед каждым тестовым методом в тестовом классе.</td>
		   </tr>
		   <tr>
				<td>@AfterEach</td>
				<td>Аннотированный метод будет запускаться после каждого тестового метода в тестовом классе.</td>
		   </tr>
		   <tr>
				<td>@BeforeAll</td>
				<td>Аннотированный метод будет запущен перед всеми тестовыми методами в тестовом классе. Этот метод должен быть статическим.</td>
		   </tr>
		   <tr>
				<td>@AfterAll</td>
				<td>Аннотированный метод будет запущен после всех тестовых методов в тестовом классе. Этот метод должен быть статическим.</td>
		   </tr>
		   <tr>
				<td>@Test</td>
				<td>Он используется, чтобы пометить метод как тест junit.</td>
		   </tr>
		   <tr>
				<td>@DisplayName</td>
				<td>Используется для предоставления любого настраиваемого отображаемого имени для тестового класса или тестового метода</td>
		   </tr>
		   <tr>
				<td>@Disable</td>
				<td>Он используется для отключения или игнорирования тестового класса или тестового метода из набора тестов.</td>
		   </tr>
		   <tr>
				<td>@Nested</td>
				<td>Используется для создания вложенных тестовых классов</td>
		   </tr>
		   <tr>
				<td>@Tag</td>
				<td>Пометьте методы тестирования или классы тестов тегами для обнаружения и фильтрации тестов.</td>
		   </tr>
		   <tr>
				<td>@TestFactory</td>
				<td>Отметить метод - это тестовая фабрика для динамических тестов.</td>
		   </tr>
		</table>
	</p>
	<p>В файле TestAuthorization.java описать автотест следующим образом
		<pre><code>
package tests;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

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

    @BeforeAll
    public static void before(){
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @Tag("PROD")
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
        Assertions.assertEquals(text, "Authorization was successful");
    }

    @AfterAll
    public static void after(){
        driver.close();
        driver.quit();
    }
}
		</code></pre>
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_junit.jpg">
		</p>
	</p>
	<p>Запустить автотеста в среде IntelliJ IDEA и убедится что всё работает корректно
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_junit_run.jpg">
		</p>
	</p>
</p>
<hr>
<p>
	<h2>Описание паттернов PageObjects и StepObjects</h2>
	<p>Описать паттерны PageObjects и StepObjects организовав структуру пакета support следующим образом:</p>
	<p>Файл Helper.java - описаны константы
		<pre><code>
package support;

public class Helper {
    public static String URL = "https://somovstudio.github.io/test_eng.html";
    public static String LOGIN = "admin";
    public static String PASSWORD = "0000";
}
		</code></pre>
	</p>
	<p>Файл CommonPage.java - описаны локаторы и статичные методы
		<pre><code>
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
        WebElement element = driver.findElement(By.id(CommonPage.
                               idResult));
        Wait<WebDriver> wait = new WebDriverWait(driver,
                               Duration.ofSeconds(5));
        wait.until(d -> element.isDisplayed());
        String text = driver.findElement(By.id(CommonPage.
                               idTextarea)).getAttribute("value");
        System.out.println("Get message: " + text);
        return text;
    }
}
		</code></pre>
	</p>
	<p>Файл CommonSteps.java - описан класс методов для выполнения действий
		<pre><code>
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
        driver.findElement(
              By.name(CommonPage.nameLogin)).sendKeys(login);
        driver.findElement(
              By.name(CommonPage.namePassword)).sendKeys(password);
        driver.findElement(
              By.id(CommonPage.idButtonLogin)).click();
    }
}
		</code></pre>
	</p>
	<p>Файл автотеста TestAuthorization2.java - используются ранее описанные паттерны
		<pre><code>
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
		</code></pre>
	</p>
	<p align="left">
		<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_patterns.jpg">
	</p>
</p>
<hr>
<p>
	<h2>Запуск автотестов с помощью Apache Maven</h2>
	<p>Скачать и установить <a href="https://maven.apache.org/download.cgi">Apache Maven</a> (архив: apache-maven-3.9.9-bin.zip)</p>
	<p>Подключить плагин Maven Surefire Plugin к проекту в файле pom.xml
		<br>ссылка: https://mvnrepository.com/artifact/org.apache.maven.plugins/maven-surefire-plugin
		<br>ссылка: https://mvnrepository.com/artifact/org.junit.jupiter/junit-jupiter-engine
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_pom_maven_plagin.jpg">
		</p>
	</p>
	<p>Создать <a href="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/selenium/java/example-junit/run.bat">run.bat</a> файл для запуска автотеста из командной строки с помощью Maven
		<pre><code>
E:
cd E:\Git\SomovQA\Practice-Automation-Testing-2024\selenium\java\example-junit
"C:\Program Files\apache-maven-3.9.9\bin\mvn" clean test -Dtest=TestAuthorization
		</code></pre>
		<p>Запустить файл run.bat</p>
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_junit_console_run.jpg">
		</p>
		<p>Автотест будет запущен и выполнен.</p>
	</p>
</p>
<hr>
<p>
	<h2>Практика применения TestNG</h2>
	<p>Подключить библиотеку TestNG к проекту в файле pom.xml
		<br> ссылка: <a href="https://mvnrepository.com/artifact/org.testng/testng">https://mvnrepository.com/artifact/org.testng/testng</a>
		<pre><code>
< dependency >
	< groupId >org.testng< /groupId >
	< artifactId >testng< /artifactId >
	< version >7.10.2< /version >
	< scope >test< /scope >
< /dependency >
		</code></pre>
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_pom_testng.jpg">
		</p>
	</p>
	<p>В папке test создать пакет tests</p>
	<p>В пакете tests создать класс автотеста TestAuthorization.java</p>
	<p>В файле TestAuthorization.java описать автотест следующим образом
		<pre><code>
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
		</code></pre>
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_testng.jpg">
		</p>
	</p>
	<p>Запустить автотеста в среде IntelliJ IDEA и убедится что всё работает корректно
		<p align="left">
			<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_test_testng_run.jpg">
		</p>
	</p>
</p>