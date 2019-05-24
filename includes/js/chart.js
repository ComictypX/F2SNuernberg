function loadChart(chartName) {
	
	// console.log("logging, chartName = ", chartName);
	var xdatapoints;
	if (chartName == "MonthChart") {
		xdatapoints = 30;
	}
	else if (chartName == "3MonthChart") {
		xdatapoints = 9;
	}
	else if (chartName == "YearChart") {
		xdatapoints = 12;
	}
	else if (chartName == "AllChart") {
		xdatapoints = 12;
	}

	var chartdata = []

	for (var i = 1; i < xdatapoints + 1; i += 1) {
		y = 30 + 2*Math.random();
		chartdata.push({
			x: i,
			y: y
		});
	}

	var chart = new CanvasJS.Chart(chartName, {
	  animationEnabled: true,
	  theme: "light2",
	  axisY:{
		includeZero: false
	  },
	  data: [{        
		type: "line",       
		dataPoints: chartdata
	  }]
	});
	chart.render();

	// var chart = new CanvasJS.Chart("3MonthChart", {
	// 	animationEnabled: true,
	// 	theme: "light2",
	// 	title:{
	// 	  text: "Eco History"
	// 	},
	// 	axisY:{
	// 	  includeZero: false
	// 	},
	// 	data: [{        
	// 	  type: "line",       
	// 	  dataPoints: [
	// 		{ y: 450 },
	// 		{ y: 414 },
	// 		{ y: 520 },
	// 		{ y: 460 },
	// 		{ y: 450 },
	// 		{ y: 500 },
	// 		{ y: 480 },
	// 		{ y: 480 },
	// 		{ y: 410 },
	// 		{ y: 500 },
	// 		{ y: 480 },
	// 		{ y: 510 }
	// 	  ]
	// 	}]
	//   });
	//   chart.render();

	//   var chart = new CanvasJS.Chart("YearChart", {
	// 	animationEnabled: true,
	// 	theme: "light2",
	// 	title:{
	// 	  text: "Eco History"
	// 	},
	// 	axisY:{
	// 	  includeZero: false
	// 	},
	// 	data: [{        
	// 	  type: "line",       
	// 	  dataPoints: [
	// 		{ y: 450 },
	// 		{ y: 414 },
	// 		{ y: 520 },
	// 		{ y: 460 },
	// 		{ y: 450 },
	// 		{ y: 500 },
	// 		{ y: 480 },
	// 		{ y: 480 },
	// 		{ y: 410 },
	// 		{ y: 500 },
	// 		{ y: 480 },
	// 		{ y: 510 }
	// 	  ]
	// 	}]
	//   });
	//   chart.render();

	//   var chart = new CanvasJS.Chart("AllChart", {
	// 	animationEnabled: true,
	// 	theme: "light2",
	// 	title:{
	// 	  text: "Eco History"
	// 	},
	// 	axisY:{
	// 	  includeZero: false
	// 	},
	// 	data: [{        
	// 	  type: "line",       
	// 	  dataPoints: [
	// 		{ y: 450 },
	// 		{ y: 414 },
	// 		{ y: 520 },
	// 		{ y: 460 },
	// 		{ y: 450 },
	// 		{ y: 500 },
	// 		{ y: 480 },
	// 		{ y: 480 },
	// 		{ y: 410 },
	// 		{ y: 500 },
	// 		{ y: 480 },
	// 		{ y: 510 }
	// 	  ]
	// 	}]
	//   });
	//   chart.render();
	
	}