# Selenium (Java)

Автоматизированное тестирование Selenium на языке Java

<p>
	<h4>Содержание:</h2>
	<ul>
		<li>example-simple</li>
		<li>example-junit</li>
		<li>example-testng</li>
		<li>demo</li>
	</ul>
</p>

<p>
	<h4>Полезные ссылки:</h2>
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
	<h4>Практика применения JUnit</h4>
	<ol>
		<li>Подключить библиотеку JUnit Jupiter API к проекту в файле pom.xml
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
		</li>
		<li>В папке test создать пакет tests
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_create_package.jpg">
			</p>
		</li>
		<li>В пакете tests создать класс автотеста TestAuthorization.java
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/java_create_test.jpg">
			</p>
		</li>
		<li></li>
		<li></li>
		<li></li>
	</ol>
</p>