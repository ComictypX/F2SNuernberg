window.onload = function () {
  console.log("window load ");
  // loadJSON(function(response) {
    // Parse JSON string into object
  //     var actual_JSON = JSON.parse(response);
  //  });
}

function loadJSON(callback) {
  file = "../data/batteryData.json"
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType('application/json');
  xobj.open('GET', file, true); 
  console.log("window load 1");
  xobj.onreadystatechange = function () {
    if (xobj.readyState == 4 && xobj.status == '200') {
      console.log("window load 2");
    // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
      callback(xobj.responseText);
     }
  };
  xobj.send(null);
}