window.onload = function(){
    new Chartist.Bar('.quality_chart', {
        labels: ['98,5', '98,75', '98,75', '101', '101', '100', '100'],
        series: [98.5, 98.75, 98.75, 101, 101, 100, 100]
      }, {
        distributeSeries: true
      });
};