const $ = (s) => document.querySelector(s);

const GALLERY = [
	{
		title: "Вера, 29 лет, няня со стажем",
		img: {
			src: "src/pictures/nanny1.jpg",
			alt: "Няня Вера",
			title: "Няня Вера",
		},
	},
	{
		title: "Евграф Витальевич, 41 год, ветеринар",
		img: {
			src: "src/pictures/nanny2.jpg",
			alt: "Евграф Витальевич, ветеринар",
			title: "Оставить питомца с профессионалом",
		},
	},
	{
		title: "Анна, 35 лет, орнитолог",
		img: {
			src: "src/pictures/nanny3.jpeg",
			alt: "Орнитолог Анна и ее попугай",
			title: "Няня питомцу",
		},
	},
	{
		title: "Алена, 19 лет, просто любит животных",
		img: {
			src: "src/pictures/nanny4.png",
			alt: "Песоняня Алена со своим псом",
			title: "Няня для собачки",
		},
	},
	{
		title: "Марианна, 25 лет, хозяйка приюта для котиков",
		img: {
			src: "src/pictures/nanny5.jpeg",
			alt: "Хозяйка котоприюта Марианна",
			title: "Марианна присмотрит за вашим котиком",
		},
	},
];

const initGallery = (function () {
	const createContent = function (content) {
		const $creaBlock = document.createElement("figure");
		$creaBlock.classList.add("creaBlock");
		$creaBlock.classList.add("creaBlockPrez");
		const $lineSeparator = document.createElement("div");
		$lineSeparator.classList.add("lineSeparator");
		$creaBlock.appendChild($lineSeparator);
		const $blocImg = document.createElement("div");
		$blocImg.classList.add("blocImg");
		const $img = document.createElement("img");
		$img.setAttribute("src", content.img.src);
		$img.setAttribute("alt", content.img.alt);
		$img.setAttribute("title", content.img.title);
		$blocImg.appendChild($img);
		$creaBlock.appendChild($blocImg);
		const $title = document.createElement("figcaption");
		$title.innerText = content.title;
		$creaBlock.appendChild($title);
		return $creaBlock;
	};
	const $galleryBloc = document.createElement("div");
	const $galleryContent = document.createElement("div");
	$galleryContent.classList.add("creationsBlocUl");
	GALLERY.forEach((e, index) => $galleryContent.appendChild(createContent(e)));
	$galleryBloc.appendChild($galleryContent);
	$("#nannys_cards").appendChild($galleryBloc);
})();
