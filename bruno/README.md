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
			</code></pre>
			<br>таким образом API будет по адресу http://localhost/api/auth.php?name=admin&pass=0000
		</li>
		<li>Скачать и установить <a href="https://docs.usebruno.com/">Bruno</a></li>
		<li>Запустить Bruno и создать коллекцию tests
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_create_collection.jpg">
			</p>
		</li>
		<li>В коллекции tests создать запрос Test01
		<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_new_request.jpg">
			</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_new_request_data.jpg">
			</p>
			<p>Выбрать однин из режимов (safe - ограниченный, Developer - полный)</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_new_request_mode.jpg">
			</p>
		</li>
		<li>В новом запросе указать параметры
			<pre><code>
name: admin
pass: 0000
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_params.jpg">
			</p>
			<p>и заголовок</p>
			<pre><code>
Content-type: application/json; charset=UTF-8
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_headers.jpg">
			</p>
			<p>нажать кнопку сохранить</p>
		</li>
		<li>Выполните запрос
			<p>В результате сервер должен ответит:</p>
			<pre><code>
{"status":"PASSED","message":"Авторизация прошла успешно"}
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_get_run.jpg">
			</p>
			<p>Для того чтобы выполнить POST запрос параметры нужно передавать через Body</p>
			<pre><code>
post_name: admin
post_pass: 0000
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_post_run.jpg">
			</p>
		</li>
		<li>Простая проверка в которой определяется ответ сервера, если 200 значит успешно
			<pre><code>
test("Проверить ответ сервера", function() {
  const data = res.getBody();
  expect(res.getStatus()).to.equal(200);
});
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_test.jpg">
			</p>
			<p>Эту проверку можно выполнить без скрипта на вкладке Assert</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_assert.jpg">
			</p>
		</li>
		<li>Выполним проверку сообщения возвращаемого сервером
			<p>Создадим POST запрос и на вкладке Script пропишем отправляемые данные</p>
			<pre><code>
req.setBody({
  "post_name": "admin",
  "post_pass": "0000"
});
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_script.jpg">
			</p>
			<p>на вкладке Tests добавим проверку сообщения полученного от сервера</p>
			<pre><code>
test("Проверить сообщения частично", function() {
  const data = res.getBody();
  expect(data.message).to.contains('успешно');
});

test("Проверить сообщения полностью", function() {
  const data = res.getBody();
  expect(data.message).to.equal('Авторизация прошла успешно');
});

test("Проверить тип сообщения строка", function() {
  const data = res.getBody();
  expect(data.message).to.be.a('string');
});
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_tests.jpg">
			</p>		
		</li>
		<li>Выполним запрос
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_request_results.jpg">
			</p>
			<p>В результате будет проверено сообщение частично и полностью, а так же проверен тим поля.</p>
		</li>
		<li>Запуск тестов из командной строки
			<p>
				Скачайте и установите <a href="https://nodejs.org/">NodeJS</a>
				<br>Откройте консоль и выполните установку 
			</p>
			<pre><code>
npm install -g @usebruno/cli
			</code></pre>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_install_userbruno_cli.jpg">
			</p>
			<p>Перейдите в каталог, где находится коллекция запросов и выполните следующую команду:</p>
			<pre><code>
bru run test02.bru
			</code></pre>
			<p>результат выполнения будет отражен в консоли</p>
			<p align="left">
				<img src="https://github.com/Somov-QA/Practice-Automation-Testing-2024/blob/main/_images/bruno_cli_run.jpg">
			</p>
		</li>
	</ol>
</p>
