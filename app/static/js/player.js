var app = app || {};



window.addEventListener('DOMContentLoaded', (event) => {
	app.jams = JSON.parse(document.getElementById('jams').innerText);
	Amplitude.init({
		"songs": app.jams,
	});

});
