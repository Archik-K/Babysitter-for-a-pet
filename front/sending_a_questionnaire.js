document
	.getElementById("sending_a_babysitter_questionnaire")
	.addEventListener("click", function () {
		var xhr = new XMLHttpRequest();
		xhr.open("GET", "http://localhost:5000/nanny", true);

		xhr.onreadystatechange = function () {
			if (xhr.readyState === 4 && xhr.status === 200) {
				var response = JSON.parse(xhr.responseText);
				// Обработка ответа от сервера
				console.log(response);
			}
		};
		xhr.send();
	});
