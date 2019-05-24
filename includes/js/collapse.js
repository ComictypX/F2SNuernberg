window.onload = function () {

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }

    console.log("coll localName = , i ", i);
    if (i == 1) {
      changeHighscoreTab(event, 'Overall score');
    }
    else if (i == 2) {
      changeChartTab(event, 'MonthChart');
    };
  });
}


}