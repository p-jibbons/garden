$(function () {

  var $measurementChart = $("#measurement-chart");
  $.ajax({
    url: $measurementChart.data("url"),
    success: function (data) {

      var ctx = $measurementChart[0].getContext("2d");

      new Chart(ctx, {
        type: 'bar',
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


scales: {
                yAxes: [{
                        display: true,
                        labelString: 'Plant Measurement',
                        ticks: {
                            min: 0,
                            max: 100,
                            stepSize:20
                        }
                    }]
            }





        }
      });

    }
  });

});