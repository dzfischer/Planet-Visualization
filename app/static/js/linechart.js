$(function() {
  var data_2016 = [];
  for (var i = 0; i < 12; i++) {
    data_2016.push(monthly[i]["net_points"]);
  }
  var data_2017 = [];
  for (var i = 12; i < 24; i++) {
    data_2017.push(monthly[i]["net_points"]);
  }
  var data_2018 = [];
  for (var i = 24; i < 36; i++) {
    data_2018.push(monthly[i]["net_points"]);
  }
  var data_2019 = [];
  for (var i = 36; i < monthly.length; i++) {
    data_2019.push(monthly[i]["net_points"]);
  }
  // Line chart
  new Chart(document.getElementById("consumption_chart"), {
    type: "line",
    data: {
      labels: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
      ],
      datasets: [
        // {
        //   label: "2016",
        //   fill: true,
        //   backgroundColor: "transparent",
        //   borderColor: window.theme.success,
        //   borderDash: [8, 8],
        //   data: data_2016
        // },
        // {
        //   label: "2017",
        //   fill: true,
        //   backgroundColor: "transparent",
        //   borderColor: window.theme.danger,
        //   borderDash: [4, 4],
        //   data: data_2017
        // },
        {
          label: "2018",
          fill: true,
          backgroundColor: "transparent",
          borderDash: [2, 2],
          borderColor: window.theme.warning,
          data: data_2018
        },
        {
          label: "2019",
          fill: true,
          backgroundColor: "transparent",
          borderColor: window.theme.primary,
          data: data_2019
        }
      ]
    },
    options: {
      maintainAspectRatio: true,
      legend: {
        display: true
      },
      tooltips: {
        intersect: false
      },
      hover: {
        intersect: true
      },
      plugins: {
        filler: {
          propagate: false
        }
      },
      scales: {
        xAxes: [
          {
            reverse: true,
            gridLines: {
              color: "rgba(0,0,0,0.05)"
            }
          }
        ],
        yAxes: [
          {
            ticks: {
              stepSize: 50000
            },
            display: true,
            borderDash: [5, 5],
            gridLines: {
              color: "rgba(0,0,0,0.05)",
              fontColor: "#000000"
            }
          }
        ]
      }
    }
  });
});
