function sendDataToServer(data) {
	// Опции для POST-запроса
	const requestOptions = {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(data),
	};

	// Выполняем POST-запрос с помощью Fetch API
	fetch("http://localhost:5000/nanny", requestOptions)
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

// Обработчик события для кнопки "Отправить"
document
	.getElementById("sending_a_babysitter_questionnaire")
	.addEventListener("click", function () {
		// Получаем данные из формы
		const name = document.getElementById("nameForm").value;
		const image = document.querySelector(".image_nanny").files[0]; // Вам нужно обработать загрузку изображения вручную, если необходимо
		const selection = document.querySelector(".form-select").value;
		const phone = document.getElementById("phoneForm").value;
		const preferredContactMethod = document.getElementById("flexRadioDefault1")
			.checked
			? "Мобильная связь"
			: "Мессенджер";
		const username = document.querySelector(".input-group input").value;
		const email = document.getElementById("emailForm").value;
		const birthDate = document.querySelector('input[name="calendar"]').value;
		const additionalComments = document.getElementById("commentsForm").value;

		// Создаем объект для отправки данных
		const data = {
			name,
			image, // Вам нужно обработать загрузку изображения вручную, если необходимо
			selection,
			phone,
			preferredContactMethod,
			username,
			email,
			birthDate,
			additionalComments,
		};

		// Выполняем POST-запрос
		sendDataToServer(data);
	});
