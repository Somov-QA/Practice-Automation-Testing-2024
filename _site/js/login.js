(function(){

	function test(){
		alert('OK');
	}

	var loginInputName = document.getElementById('login');
	var loginInputPass = document.getElementById('pass');
	var loginButton = document.getElementById('buttonLogin');

	loginButton.addEventListener('click', function(){
		document.getElementById('result').style = 'visibility: visible';
		if(loginInputName.value == 'admin' && loginInputPass.value == '0000'){
			document.getElementById('textarea').value = 'Authorization was successful';
		}else{
			document.getElementById('textarea').value = 'Invalid login or password';
		}
	});

}());