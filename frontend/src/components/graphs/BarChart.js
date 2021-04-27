import { Bar, mixins } from 'vue-chartjs'
import ChartJSPluginDatalabels from 'chartjs-plugin-datalabels'
const { reactiveProp } = mixins

export default {
    extends: Bar,
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
                plugins: {
                    datalabels: {
                        color: 'black',
                        display: function(context) {
                            return context.dataset.data[context.dataIndex] > 0
                        },
                        font: {
                            weight: 'bold',
                        },
                        formatter: Number.toFixed,
                    },
                },
                scales: {
                    xAxes: [
                        {
                            // barPercentage: 0.5,
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
                                display: true,
                                color: 'transparent',
                                zeroLineColor: '#E5E5E5',
                            },
                            ticks: {
                                display: false,
                                max: 102,
                                min: 97.5,
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
