$(function () {
      var $measurementRadarChart = $("#measurement-radar-chart");
      $.ajax({
        url: $measurementRadarChart.data("url"),
        success: function (data) {

          var ctx = $measurementRadarChart[0].getContext("2d");

          new Chart(ctx, {
            type: 'radar',
            data: {
              labels: data.labels,
              datasets: [{
                label: 'Measurement',
                backgroundColor: 'blue',
                data: data.data
              }]
            },
            options: {
              responsive: true,
              legend: {position: 'top',},
              title: {display: true,text: 'Plant Measurement Radial Chart'},


              scale: {
                ticks: {
                  suggestedMin: 0,
                  suggestedMax: 100
                        }
                      }



            }
          });

        }
      });

    });