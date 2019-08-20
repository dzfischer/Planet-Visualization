$(function() {
  var cacc = meetings.filter(function(fil) {
      if (fil.event_type_group == "Corporate Access") {
        return true;
      }
      return false;
    }).map(function(e) {
      return e.total;
    });
    var rsvc = meetings.filter(function(fil) {
      if (fil.event_type_group == "Research Services") {
        return true;
      }
      return false;
    }).map(function(e) {
      return e.total;
    });
    var models = meetings.filter(function(fil) {
      if (fil.event_type_group == "Research Content") {
        return true;
      }
      return false;
    }).map(function(e) {
      return e.total;
    });
    console.log(cacc);
    console.log(rsvc);
    console.log(models);
  var config = {
    type: "line",
    data: {
      labels: ["January", "February", "March", "April", "May", "June", "July", "August"],
      datasets: [
        {
          label: "Corporate Access",
          borderColor: window.theme.danger,
          backgroundColor: window.theme.danger,
          data: cacc
        },
        {
          label: "Research Services",
          borderColor: window.theme.success,
          backgroundColor: window.theme.success,
          data: rsvc
        },
        {
          label: "Models & Content",
          borderColor: window.theme.info,
          backgroundColor: window.theme.info,
          data: models
        }
      ]
    },
    options: {
      maintainAspectRatio: true,
      responsive: true,
      tooltips: {
        mode: "index",
        intersect: false
      },
      hover: {
        mode: "index"
      },
      scales: {
        xAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Month"
            }
          }
        ],
        yAxes: [
          {
            stacked: true,
            scaleLabel: {
              display: true,
              labelString: "Value"
            }
          }
        ]
      }
    }
  };

  //stacked area
  new Chart(document.getElementById("stacked_chartjs"), config);
});
