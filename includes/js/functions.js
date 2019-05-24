var data = [];

function process(obj) // Ajax return verarbeiten
{
    if (obj.search("Startzeit") != -1) // wenn config
    {
        data = JSON.parse(obj);
        audio.volume = config.Signalton_vol / 100;
    } else if (obj.search("Farbe") != -1) // wenn timetable
    {
        timetable = JSON.parse(obj);

    } else { // wenn GPIO

        gpio = obj;
    }


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
    
    pollServer("./scripts/readini.php");
    pollServer("./scripts/readcsv.php");
    updateMap(45.00, 0, 1500);
    jetzt = new Date();
    return;
}
function run() { // Grundlogik
    console.log("Ouch");
	// Daten holen
    refresh();
    return;

}