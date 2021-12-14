import justpy as jp
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
data= pandas.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv", parse_dates=['Date'])

data['Year']= data['Date'].dt.year
data.head()
day_average = data.groupby(['Year']).mean()

chart_def = """
{
chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Year'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Fatalities'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Fatalities',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Airplane Crushes", classes="text-h2 text-right q-pt-xs")
    p1 = jp.QDiv(a=wp, text="These graphs represent the analysis of crushes from 1908 till 2009", classes="text-h5 text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Fatalties by Year"

    hc.options.xAxis.categories = list(day_average.index)


    hc.options.series[0].data = list(day_average['Fatalities'])
    return wp
jp.justpy(app)
