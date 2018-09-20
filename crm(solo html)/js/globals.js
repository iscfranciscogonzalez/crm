var xhr = new XMLHttpRequest();;
function loadDocument(){
	xhr.open('GET', 'globalhtml/navbar.html');
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4 && xhr.status == 200){
			document.getElementById('navbar').innetHTML = xhr.responseText;
		}
	}
	xhr.send();
}