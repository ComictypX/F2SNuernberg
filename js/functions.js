var data = [];

function process(obj) // Ajax return verarbeiten
{
    console.log(obj);
    data = JSON.parse(obj);
    console.log(data);
}

function statechange() {
    if (this.readyState == 4) {
        process(this.responseText);

    }
}

function pollServer(pfad) {
    try {
        var request = new XMLHttpRequest();

        if (request) {
            request.onreadystatechange = statechange;
            request.open("GET", pfad, true);
            request.send(null);

        } else {
            alert("XMLHttpRequest failed");

            clearInterval(timer);
        }
    } catch (err) {
        alert(err.description);

        clearInterval(timer);
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function refresh() {
    // Daten aktualisieren
    console.log("Updating");
    //Map update
    
    pollServer("includes/scripts/getJson.php");
    updateMap(49.4773575,11.1156473, 1500);
    
    jetzt = new Date();
    return;
}
function run() { // Grundlogik
    console.log("Ouch");
	// Daten holen
    refresh();
    return;

}