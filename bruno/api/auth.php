<?php

header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

date_default_timezone_set("Europe/Moscow");

/*	
	Пример обращения к этому API
	http://localhost/api/auth.php?name=admin&pass=0000
*/

if ($_GET["name"] == "admin" && $_GET["pass"] == "0000")
{
	print('{"status":"PASSED","message":"Авторизация прошла успешно"}');
}
else{
	print('{"status":"FAILED","message":"Некорректный логин или пароль"}');
}

?>