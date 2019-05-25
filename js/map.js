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
		mymap.setView([lat, long]);
		marker.setLatLng([lat, long]).update();
		circle.setLatLng([lat, long]);
		circle.setRadius(range);  
	}


function listMarker(){

	var greenIcon = L.icon({
    iconUrl: 'images/google-map-maker.png',
   

    iconSize:     [25, 40], // size of the icon
    shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});


	var i;
	var LatList =[49.478128,49.474415,49.474942,49.472013, 49.432688];
 var litLong=[11.108415,11.097269,11.116344, 11.134430, 11.049539];


	for (i = 0; i < LatList.length; i++) { 

	marker = L.marker([LatList[i],litLong[i]], {icon: greenIcon}).addTo(mymap);

	console.log("test");
	console.log(LatList[i]);
	console.log(litLong[i]);
  }	
}

