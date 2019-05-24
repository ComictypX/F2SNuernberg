
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>
   <script type="text/javascript" src="/includes/js/map.js"></script> 
   
<div id="map-canvas" style="height: 500px; width: 800px; margin: 100px auto;"></div>

<script>

//Map initialize
initMap(51.505, -0.09, 800);

//Map update
console.log("Updating");
updateMap(45.00, 0, 1500);




</script>