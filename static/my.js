
var chart;
$(document).ready(function() {

    $('#popup').show("bounce", { times:3 }, 300);
    $('.showpop').hide();
    $('.hiden').click(function(){
        $('#popup').slideUp();
        $('span.showpop').fadeIn('slow');
        return false;
    });

    $('a.showpoplink').click(function(){
        $('#popup').show("bounce", { times:3 }, 300);
        $('.showpop').hide();
        return false;
    });


    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container_week',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: '一个礼拜中的每一天'
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.point.name +'</b>: '+ Highcharts.numberFormat(this.percentage, 1) +' %';
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: Highcharts.theme.textColor || '#000000',
                    connectorColor: Highcharts.theme.textColor || '#000000',
                    formatter: function() {
                        return '<b>'+ this.point.name +'</b>: '+ Highcharts.numberFormat(this.percentage, 1) +' %';
                    }
                }
            }
        },
        series: [{
                type: 'pie',
                name: 'Browser share',
                data: ${value3}
            }]
    });
});


var chart1;
jQuery(document).ready(function() {
    chart1 = new Highcharts.Chart({
        chart: {
            renderTo: 'container_combin'
        },
        title: {
            text: '各时段统计图'
        },
        xAxis: {
            categories: ['0:00~3:59', '4:00~7:59', '8:00~11:59', '12:00~15:59', '16:00~19:59','20:00~23:59']
        },
        yAxis: {

        },
        tooltip: {
            formatter: function() {
                var s;
                if (this.point.name) { // the pie chart
                    s = ''+
                        this.point.name +': '+Highcharts.numberFormat(this.percentage, 1) +' %';
                } else {
                    s = ''+
                        this.x  +': '+ this.y+'+ ';
                }
                return s;
            }
        },
        labels: {
            items: [{
                    html: '早、中、晚微博数量',
                    style: {
                        left: '50px',
                        top: '8px',
                        color: 'black'
                    }
                }]
        },
        series: [{
                type: 'column',
                name: '0h',
                data: ${combin[0]}
            }, {
                type: 'column',
                name: '1h',
                data: ${combin[1]}
            }, {
                type: 'column',
                name: '2h',
                data: ${combin[2]}
            },
            {
                type: 'column',
                name: '3h',
                data: ${combin[3]}
            }, {
                type: 'spline',
                name: 'Average',
                data: ${combin[4]}
            }, {
                type: 'pie',
                name: 'Total consumption',
                data: ${combin[5]},
                center: [100, 80],
                size: 100,
                showInLegend: false,
                dataLabels: {
                    enabled: false
                }
            }]
    });


});




var chart2;
$(document).ready(function() {
    chart2 = new Highcharts.Chart({
        chart: {
            renderTo: 'container_zhuanf',
            defaultSeriesType: 'line',
            zoomType: 'xy'
        },
        title: {
            text: '一个月份中的每一天'
        },
        subtitle: {
            <!--text: 'Source: Heinz  2003'-->
        },
        xAxis: {
            title: {
                enabled: true,
                text: '日期/号'
            },
            startOnTick: false,
            endOnTick: false,
            showLastLabel: false
        },
        yAxis: {
            title: {
                text: '',
                style: {
                    color: '#000000',
                    fontWeight: 'bold'
                }

            }


        },
        tooltip: {
            formatter: function() {
                return ''+
                    this.x +' 号, '+ this.y +' +';
            }
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            shadow: true,
            itemStyle: {
                cursor: 'pointer',
                color: '#000000',
                fontWeight: 'bold'
            },
            verticalAlign: 'top',
            x: 30,
            y: 70,
            floating: false,
            backgroundColor: Highcharts.theme.legendBackgroundColor || '#FFFFFF',
            borderWidth: 1
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 6,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: true
                        }
                    }
                }
            }
        },
        series: [{
                name: '转发数',
                color: 'rgba(223, 83, 83, .5)',
                data: ${zhuanf}

            },{
                name: '原创数',
                color: 'rgba(119, 152, 191, .5)',
                data: ${fzhuanf}

            },{
                name: '总共数',
                <!--                            color: 'rgba(119, 152, 191, .5)',-->
                data: ${f_total}
            }]
    });


});


var chart3;
var index =false;
$(document).ready(function() {
    var colors = Highcharts.getOptions().colors,
    categories = ['MSIE', 'Firefox', 'Chrome', 'Safari', 'Opera'],
    categories = ["Jan","Feb","Mar","Apr","May","June","Jul","Aug","Sep","Oct","Nov","Dec"],
    name = 'The year of 2012',
    data = [{
            y: 55.11,
            color: colors[0],
            drilldown: {
                name: 'MSIE versions',
                categories: ['MSIE 6.0', 'MSIE 7.0', 'MSIE 8.0', 'MSIE 9.0'],
                data: [10.85, 7.35, 33.06, 2.81],
                color: colors[0]
            }
        }, {
            y: 21.63,
            color: colors[1],
            drilldown: {
                name: 'Firefox versions',
                categories: ['Firefox 2.0', 'Firefox 3.0', 'Firefox 3.5', 'Firefox 3.6', 'Firefox 4.0'],
                data: [0.20, 0.83, 1.58, 13.12, 5.43],
                color: colors[1]
            }
        }, {
            y: 11.94,
            color: colors[2],
            drilldown: {
                name: 'Chrome versions',
                categories: ['Chrome 5.0', 'Chrome 6.0', 'Chrome 7.0', 'Chrome 8.0', 'Chrome 9.0',
                    'Chrome 10.0', 'Chrome 11.0', 'Chrome 12.0'],
                data: [0.12, 0.19, 0.12, 0.36, 0.32, 9.91, 0.50, 0.22],
                color: colors[2]
            }
        }, {
            y: 7.15,
            color: colors[3],
            drilldown: {
                name: 'Safari versions',
                categories: ['Safari 5.0', 'Safari 4.0', 'Safari Win 5.0', 'Safari 4.1', 'Safari/Maxthon',
                    'Safari 3.1', 'Safari 4.1'],
                data: [4.55, 1.42, 0.23, 0.21, 0.20, 0.19, 0.14],
                color: colors[3]
            }
        }, {
            y: 2.14,
            color: colors[4],
            drilldown: {
                name: 'Opera versions',
                categories: ['Opera 9.x', 'Opera 10.x', 'Opera 11.x'],
                data: [ 0.12, 0.37, 1.65],
                color: colors[4]
            }
        }];

    function setChart(name, categories, data, color) {
        chart.xAxis[0].setCategories(categories);
        chart.series[0].remove();
        chart.addSeries({
            name: name,
            data: data,
            color: color || 'white'
        });
    }

    chart3 = new Highcharts.Chart({
        chart: {
            renderTo: 'container_year',
            type: 'column'
        },
        title: {
            text: '这里尽可能多的获取您的微博，所以载入速度会比较慢，建议使用非IE内核的浏览器...'
        },
        subtitle: {
            <!--text: '这两年（点击切换）'-->
        },
        xAxis: {
            categories: categories
        },
        yAxis: {
            title: {
                text: 'Total percent of Weibo'
            }
        },
        plotOptions: {
            column: {
                cursor: 'pointer',
                point: {
                    events: {
                        click: function() {
                            var drilldown = this.drilldown;
                            if (index){
                                drilldown = !(drilldown)
                            }

                            if (drilldown) { // drill down
                                setChart('The year of 2012', categories, ${value1});
                                index = !(index);
                            } else { // restore
                                index = !(index);
                                setChart('The year of 2011', categories, ${value2});
                            }
                        }
                    }
                },
                dataLabels: {
                    enabled: true,
                    color: colors[0],
                    style: {
                        fontWeight: 'bold'
                    },
                    formatter: function() {
                        return this.y +'条';
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                var point = this.point,
                s = this.x +':<b>'+ this.y +'条 Weibo</b><br/>';
                if (point.drilldown) {
                    s += 'Click to view '+ point.category +' versions';
                } else {
                    s += 'Click to return next year';
                }
                return s;
            }
        },
        series: [{
                name: name,
                data: ${value1},
                color: 'white'
            }],
        exporting: {
            enabled: false
        }
    });


});
