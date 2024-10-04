# Bruno

Тестирование API

<p>
	<h4>Содержание:</h2>
	<ul>
		<li>api - в папке содерзится пример тестируемого api</li>
		<li>tests - в папке содержаться примеры тестов</li>
	</ul>
</p>

<p>
	<h4>Полезные ссылки:</h2>
	<ul>
		<li>Официальная страница Wampserver <a href="https://www.wampserver.com/">https://www.wampserver.com/</a></li>
		<li>Официальная страница NodeJS<a href="https://nodejs.org/">https://nodejs.org/</a></li>
		<li>Официальная страница Bruno <a href="https://docs.usebruno.com/">https://docs.usebruno.com/</a></li>
		<li>Официальная документация API Testing<a href="https://docs.usebruno.com/testing/introduction">https://docs.usebruno.com/testing/introduction</a></li>
		<li>Официальная документация Scripting <a href="https://docs.usebruno.com/scripting/getting-started">https://docs.usebruno.com/scripting/getting-started</a></li>
		<li>Официальная документация CLI <a href="https://docs.usebruno.com/bru-cli/overview">https://docs.usebruno.com/bru-cli/overview</a></li>
	</ul>
</p>

<p>
	<h4>Тестирование API с помощью Bruno</h4>
	<ol>
		<li>Скачать и установить <a href="https://www.wampserver.com/">Wampserver</a> (сервер Apache, PHP, MySQL)</li>
		<li>Создать на сервере тестовое API в папке \wamp64\www\api  файл: auth.php
			<pre><code>
<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
date_default_timezone_set("Europe/Moscow");
/*	
	Пример обращения к этому API http://localhost/api/auth.php?name=admin&pass=0000
*/
if (isset($_GET["name"]) && isset($_GET["pass"]))
{
	if ($_GET["name"] == "admin" && $_GET["pass"] == "0000")
		print('{"status":"PASSED","message":"Авторизация прошла успешно"}');
	else
		print('{"status":"FAILED","message":"Некорректный логин или пароль"}');
}
elseif (isset($_POST["post_name"]) && isset($_POST["post_pass"]))
{
	if ($_POST["post_name"] == "admin" && $_POST["post_pass"] == "0000")
		print('{"status":"PASSED","message":"Авторизация прошла успешно"}');
	else
		print('{"status":"FAILED","message":"Некорректный логин или пароль"}');
}
else
{
	print('{"status":"ERROR","message":"Нет данных для авторизации"}');
}
?>
			</code></pre>
		</li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
		<li></li>
	</ol>
</p>
