var mymap = {};
var marker = {};
var circle = {};

// Initialize and add the map
function initMap(initLat, initLong, range) {
  mymap = L.map('map-canvas').setView([initLat, initLong], 13);
         L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
         'attribution':  'Kartendaten &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> Mitwirkende',
         'useCache': true
    }).addTo(mymap);
		 
	marker = L.marker([initLat, initLong]).addTo(mymap);
		 
	circle = L.circle([initLat, initLong], {
		color: 'red',
		fillColor: '#f03',
		fillOpacity: 0.5,
		radius: range
	}).addTo(mymap);
  }
  
  function updateMap( lat, long, range){
	mymap.setView([lat, long], 13);
	marker.setLatLng([lat, long]).update();
	circle.setLatLng([lat, long]);
	circle.setRadius(range);  
	}