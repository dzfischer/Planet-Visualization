function buildCharts(xaxis, yaxis) {

  // get the sample data from the /sample/<sample> path
  d3.json(`/column/${xaxis}`).then((column) => {

    var xvals = `column.${xaxis}`
    console.log xvals
  });

  d3.json(`/column/${yaxis}`).then((column) => {

    var yvals = `column.${yaxis}`
  });

  // Building a (somewhat redundant) bubble plot
  let trace = {
    x: xvals
    y: yvals
    mode: 'markers',
    // hovertext: sampleData.otu_labels,
    // marker: {
    //   size: sampleData.sample_values,
    //   color: sampleData.otu_ids
    // }
  };

  let layout = {
    title: "Title",
    margin: {
      l: 100,
      r: 100,
      t: 100,
      b: 100
    }
  };

  Plotly.newPlot('scatter', [trace], layout);
}

// ------------
buildCharts("pl_massj", "st_mass")
// ------------

function init() {
  // Grab a reference to the dropdown select elements
  var selector1 = d3.select("#selDataset1");
  var selector2 = d3.select("#selDataset2");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector1
        .append("option")
        .text(sample)
        .property("value", sample);
      selector2
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    // const firstSample = sampleNames[0];
    // buildCharts(firstSample, firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  // buildCharts(newSample);
}

// Initialize the dashboard
init();