/** the following charts are being made with /plotlychartcolumns 
    1. Planet Name (Count) vs Discovery Year
    2. Gaia Distance vs Discovery Year  ** Can I keep the same x-axis and change the y axis data? 
*/


let dataURL_disc="/planetdiscovery_dist";
d3.json(dataURL_disc).then(function(data) {
    var layout = { 
        title: 'Max Gaia Distance Traveled & Planetary Discoveries per Year ', 
        xaxis: {
            type: 'category',
            title: 'Years',
          },     
        margin: { t: 30, b: 200 } }; 
    Plotly.plot("bar", [data], layout);
    console.log(data);
});


// Get new data whenever the dropdown selection changes
function getData(route) {
    console.log(route);
    d3.json(`/${route}`).then(function(data) {
      console.log("newdata", data);
      updatePlotly(data); // to fix plotly error, put the data into arrays before graphing. Even if they are already in an array
    });
  }

// Update the plot with new data
function updatePlotly(newdata) {
    Plotly.restyle("bar", "x", [newdata.x]);
    Plotly.restyle("bar", "y", [newdata.y]);
  }



  