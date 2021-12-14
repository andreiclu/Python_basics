import justpy as jp
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
data= pandas.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv", parse_dates=['Date'])

data['Weekday'] = data['Date'].dt.strftime('%A')
data['Daynumber'] = data['Date'].dt.strftime('%w')


weekday_average = data.groupby(['Weekday', 'Daynumber']).mean()
print(weekday_average)
weekday_average = weekday_average.sort_values('Daynumber')
chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def cal():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Airplane Crushes", classes="text-h2 text-right q-pt-xs")
    p1 = jp.QDiv(a=wp, text="These graphs represent the analysis of crushes from 1908 till 2009",
             classes="text-h5 text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(weekday_average.index)

    hc_data = [{"name":v1, "data":[v2 for v2 in weekday_average[v1]]} for v1 in weekday_average.columns]

    hc.options.series = hc_data
    return wp

jp.justpy(cal)
