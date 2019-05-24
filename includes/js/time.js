
    'use strict';
    (function () {
	  function uhrzeit() {
		var jetzt = new Date(),
			h = jetzt.getHours(),
			m = jetzt.getMinutes(),
		
		m = fuehrendeNull(m);
		
		document.getElementById('uhr')
			.innerHTML = h + ':' + m+' Uhr';
		setTimeout(uhrzeit, 500);
	}

	function fuehrendeNull(zahl) {
		zahl = (zahl < 10 ? '0' : '') + zahl;
		return zahl;
	}
	document.addEventListener('DOMContentLoaded', uhrzeit);
}());