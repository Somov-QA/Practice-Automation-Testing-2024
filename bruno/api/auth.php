<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

date_default_timezone_set("Europe/Moscow");

/*	
	Пример обращения к этому API
	http://localhost/api/auth.php?name=admin&pass=0000
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