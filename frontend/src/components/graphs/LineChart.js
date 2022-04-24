import { Line, mixins } from 'vue-chartjs'
import ChartJSPluginDatalabels from 'chartjs-plugin-datalabels'
const { reactiveProp } = mixins

export default {
    extends: Line,
    mixins: [reactiveProp],
    props: {
        chartData: {
            type: Object,
        },
        options: {
            type: Object,
            default: () => ({
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    display: false,
                },
                layout:{
                  padding: {
                      left: 25,
                      right: 25,
                  }
                },
                plugins: {
                    datalabels: {
                        color: '#7c7c7c',
                        display: function(context) {
                            return context.dataset.data[context.dataIndex] > 0
                        },
                        formatter: Number.toFixed,
                    },
                },
                scales: {
                    xAxes: [
                        {
                            gridLines: {
                                display: false,
                            },
                            ticks: {
                                display: false,
                            },
                        },
                    ],
                    yAxes: [
                        {
                            gridLines: {
                                display: false,
                            },
                            ticks: {
                                display: false,
                                max: 145,
                                min: 80,
                            },
                        },
                    ],
                },
            }),
        },
    },
    mounted() {
        this.addPlugin(ChartJSPluginDatalabels)
        this.renderChart(this.chartData, this.options)
    },
}
