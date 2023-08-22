const host = "http://localhost:5000/";
const post_nanny_form = document.getElementById("post_nanny");
const button = document.querySelector("#post_nanny_button");

function post_nanny() {
	fetchOptions = {
		method: "POST",
		body: new FormData(post_nanny_form),
	};

	fetch(host + "nanny", fetchOptions)
		.then((response) => {
			if (!response.ok) {
				throw new Error("Ошибка запроса: " + response.status);
			}
			return response.json();
		})
		.then((resultData) => {
			// Обработка успешного ответа сервера
			const resultElement = document.getElementById("result");
			resultElement.innerHTML = "Результат: " + resultData.message;
		})
		.catch((error) => {
			// Обработка ошибки
			console.error(error.message);
		});
}

post_nanny_form.addEventListener("submit", (event) => {
	event.preventDefault();
});

button.addEventListener("click", post_nanny);

// Осталось сделать
// Обработка результатов запроса (10 строка)
// Чтобы фориа после запроса не обновлялась
