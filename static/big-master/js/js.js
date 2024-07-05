
$(function () {
    echarts_1();
    echarts_2();
    echarts_4();
    echarts_31();
    echarts_32();
    echarts_33();
    echarts_5();
    echarts_6();

    function echarts_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart1'));

        var option = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '4%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['北京', '上海', '广州', '深圳', '成都'],
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgb(237,238,243)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgb(248,243,243)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgb(237,238,243)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(5,5,5,0.1)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(5,5,5,0.1)",
                    }
                }
            }],
            series: [
                {
                    type: 'bar',
                    data: [32, 28, 35, 34, 29],
                    barWidth: '35%', //柱子宽度
                    // barGap: 1, //柱子之间间距
                    itemStyle: {
                        normal: {
                            color: '#2f89cf',
                            opacity: 1,
                            barBorderRadius: 5,
                        }
                    }
                }

            ],
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart2'));

        option = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: {type: 'shadow'}
            },
            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '4%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['北京', '上海', '广州', '深圳', '成都'],
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [
                {

                    type: 'bar',
                    data: [18, 20, 19, 15, 24],
                    barWidth: '35%', //柱子宽度
                    // barGap: 1, //柱子之间间距
                    itemStyle: {
                        normal: {
                            color: '#27d08a',
                            opacity: 1,
                            barBorderRadius: 5,
                        }
                    }
                }

            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart5'));

        option = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },

            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '2%',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['北京', '上海', '广州', '深圳', '成都'],
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [{
                type: 'bar',
                data: [2, 3, 3, 6, 4],
                barWidth: '35%', //柱子宽度
                // barGap: 1, //柱子之间间距
                itemStyle: {
                    normal: {
                        color: '#2f89cf',
                        opacity: 1,
                        barBorderRadius: 5,
                    }
                }
            }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_4() {
        var myChart = echarts.init(document.getElementById('echart4'));

        var option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    lineStyle: {
                        color: '#dddc6b'
                    }
                }
            },
            legend: {
                top: '0%',
                data: ['北京最高温', '北京最低温', '上海最高温', '上海最低温'],
                textStyle: {
                    color: 'rgba(255,255,255,.5)',
                    fontSize: '12',
                }
            },
            grid: {
                left: '10',
                top: '30',
                right: '10',
                bottom: '10',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                boundaryGap: false,
                axisLabel: {
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: 12,
                    },
                },
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,.2)'
                    }
                },
                data: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
            }],
            yAxis: [{
                type: 'value',
                axisTick: {show: false},
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,.1)'
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: 12,
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,.1)'
                    }
                }
            }],
            series: [
                {
                    name: '北京最高温',
                    type: 'line',
                    smooth: true,
                    data: [25, 26, 24, 28, 27, 26, 25, 27, 28, 29, 28, 27, 26, 27, 28, 29, 30, 31, 29, 28, 27, 26, 25, 27]
                },
                {
                    name: '北京最低温',
                    type: 'line',
                    smooth: true,
                    data: [15, 16, 14, 17, 16, 15, 14, 16, 17, 18, 17, 16, 15, 16, 17, 18, 19, 20, 18, 17, 16, 15, 14, 16]
                },
                {
                    name: '上海最高温',
                    type: 'line',
                    smooth: true,
                    data: [24, 25, 23, 25, 24, 23, 22, 24, 25, 26, 25, 24, 23, 24, 25, 26, 27, 28, 26, 25, 24, 23, 22, 24]
                },
                {
                    name: '上海最低温',
                    type: 'line',
                    smooth: true,
                    data: [18, 19, 17, 19, 18, 17, 16, 18, 19, 20, 19, 18, 17, 18, 19, 20, 21, 22, 20, 19, 18, 17, 16, 18]
                }
            ]
        };

        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_6() {
        var myChart = echarts.init(document.getElementById('echart6'));

        var dataStyle = {
            normal: {
                label: {show: false},
                labelLine: {show: false}
            }
        };

        var placeHolderStyle = {
            normal: {
                color: 'rgba(255,255,255,.05)',
                label: {show: false},
                labelLine: {show: false}
            },
            emphasis: {
                color: 'rgba(0,0,0,0)'
            }
        };

        var option = {
            color: ['#0f63d6', '#0f78d6', '#0f8cd6', '#0fa0d6', '#0fb4d6'],
            tooltip: {
                show: true,
                formatter: "{a} : {c} "
            },
            legend: {
                itemWidth: 10,
                itemHeight: 10,
                itemGap: 12,
                bottom: '3%',
                data: ['晴天', '雨天', '阴天'],
                textStyle: {
                    color: 'rgba(255,255,255,.6)',
                }
            },
            series: [
                {
                    name: '晴天',
                    type: 'pie',
                    clockWise: false,
                    center: ['50%', '42%'],
                    radius: ['59%', '70%'],
                    itemStyle: dataStyle,
                    hoverAnimation: false,
                    data: [{
                        value: 40,
                        name: '浙江'
                    }, {
                        value: 20,
                        name: 'invisible',
                        tooltip: {show: false},
                        itemStyle: placeHolderStyle
                    }]
                },
                {
                    name: '雨天',
                    type: 'pie',
                    clockWise: false,
                    center: ['50%', '42%'],
                    radius: ['49%', '60%'],
                    itemStyle: dataStyle,
                    hoverAnimation: false,
                    data: [{
                        value: 30,
                        name: '上海'
                    }, {
                        value: 10,
                        name: 'invisible',
                        tooltip: {show: false},
                        itemStyle: placeHolderStyle
                    }]
                },
                {
                    name: '阴天',
                    type: 'pie',
                    clockWise: false,
                    hoverAnimation: false,
                    center: ['50%', '42%'],
                    radius: ['39%', '50%'],
                    itemStyle: dataStyle,
                    data: [{
                        value: 15,
                        name: '广东'
                    }, {
                        value: 5,
                        name: 'invisible',
                        tooltip: {show: false},
                        itemStyle: placeHolderStyle
                    }]
                }
            ]
        };

        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

//
// function echarts_6() {
//         // 基于准备好的dom，初始化echarts实例
//         var myChart = echarts.init(document.getElementById('echart6'));
//
//         var dataStyle = {
// 	normal: {
// 		label: {
// 			show: false
// 		},
// 		labelLine: {
// 			show: false
// 		},
// 		//shadowBlur: 40,
// 		//shadowColor: 'rgba(40, 40, 40, 1)',
// 	}
// };
// var placeHolderStyle = {
// 	normal: {
// 		color: 'rgba(255,255,255,.05)',
// 		label: {show: false,},
// 		labelLine: {show: false}
// 	},
// 	emphasis: {
// 		color: 'rgba(0,0,0,0)'
// 	}
// };
// option = {
// 	color: ['#0f63d6', '#0f78d6', '#0f8cd6', '#0fa0d6', '#0fb4d6'],
// 	tooltip: {
// 		show: true,
// 		formatter: "{a} : {c} "
// 	},
// 	legend: {
// 		itemWidth: 10,
//         itemHeight: 10,
// 		itemGap: 12,
// 		bottom: '3%',
//
// 		data: ['浙江', '上海', '广东', '北京', '深圳'],
// 		textStyle: {
//                     color: 'rgba(255,255,255,.6)',
//                 }
// 	},
//
// 	series: [
// 		{
// 		name: '浙江',
// 		type: 'pie',
// 		clockWise: false,
// 		center: ['50%', '42%'],
// 		radius: ['59%', '70%'],
// 		itemStyle: dataStyle,
// 		hoverAnimation: false,
// 		data: [{
// 			value: 80,
// 			name: '01'
// 		}, {
// 			value: 20,
// 			name: 'invisible',
// 			tooltip: {show: false},
// 			itemStyle: placeHolderStyle
// 		}]
// 	},
// 		{
// 		name: '上海',
// 		type: 'pie',
// 		clockWise: false,
// 		center: ['50%', '42%'],
// 		radius: ['49%', '60%'],
// 		itemStyle: dataStyle,
// 		hoverAnimation: false,
// 		data: [{
// 			value: 70,
// 			name: '02'
// 		}, {
// 			value: 30,
// 			name: 'invisible',
// 			tooltip: {show: false},
// 			itemStyle: placeHolderStyle
// 		}]
// 	},
// 		{
// 		name: '广东',
// 		type: 'pie',
// 		clockWise: false,
// 		hoverAnimation: false,
// 		center: ['50%', '42%'],
// 		radius: ['39%', '50%'],
// 		itemStyle: dataStyle,
// 		data: [{
// 			value: 65,
// 			name: '03'
// 		}, {
// 			value: 35,
// 			name: 'invisible',
// 			tooltip: {show: false},
// 			itemStyle: placeHolderStyle
// 		}]
// 	},
// 		{
// 		name: '北京',
// 		type: 'pie',
// 		clockWise: false,
// 		hoverAnimation: false,
// 		center: ['50%', '42%'],
// 		radius: ['29%', '40%'],
// 		itemStyle: dataStyle,
// 		data: [{
// 			value: 60,
// 			name: '04'
// 		}, {
// 			value: 40,
// 			name: 'invisible',
// 			tooltip: {show: false},
// 			itemStyle: placeHolderStyle
// 		}]
// 	},
// 		{
// 		name: '深圳',
// 		type: 'pie',
// 		clockWise: false,
// 		hoverAnimation: false,
// 		center: ['50%', '42%'],
// 		radius: ['20%', '30%'],
// 		itemStyle: dataStyle,
// 		data: [{
// 			value: 50,
// 			name: '05'
// 		}, {
// 			value: 50,
// 			name: 'invisible',
// 			tooltip: {show: false},
// 			itemStyle: placeHolderStyle
// 		}]
// 	}, ]
// };
//
//         // 使用刚指定的配置项和数据显示图表。
//         myChart.setOption(option);
//         window.addEventListener("resize",function(){
//             myChart.resize();
//         });
//     }
    function echarts_31() {
        var myChart = echarts.init(document.getElementById('fb1'));
        option = {
            title: {
                text: '温度分布',
                left: 'center',
                textStyle: {
                    color: '#fff',
                    fontSize: '16'
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                top: '70%',
                itemWidth: 10,
                itemHeight: 10,
                data: ['低于0°C', '0-10°C', '10-20°C', '20-30°C', '30°C以上'],
                textStyle: {
                    color: 'rgba(255,255,255,.5)',
                    fontSize: '12',
                }
            },
            series: [{
                name: '温度分布',
                type: 'pie',
                center: ['50%', '42%'],
                radius: ['40%', '60%'],
                color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab'],
                data: [
                    {value: 5, name: '低于0°C'},
                    {value: 10, name: '0-10°C'},
                    {value: 15, name: '10-20°C'},
                    {value: 20, name: '20-30°C'},
                    {value: 25, name: '30°C以上'}
                ]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_32() {
        var myChart = echarts.init(document.getElementById('fb2'));
        option = {
            title: {
                text: '天气类型分布',
                left: 'center',
                textStyle: {
                    color: '#fff',
                    fontSize: '16'
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                top: '70%',
                itemWidth: 10,
                itemHeight: 10,
                data: ['晴', '阴', '小雨', '中雨', '大雨'],
                textStyle: {
                    color: 'rgba(255,255,255,.5)',
                    fontSize: '12',
                }
            },
            series: [{
                name: '天气类型分布',
                type: 'pie',
                center: ['50%', '42%'],
                radius: ['40%', '60%'],
                color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab'],
                data: [
                    {value: 20, name: '晴'},
                    {value: 15, name: '阴'},
                    {value: 10, name: '小雨'},
                    {value: 5, name: '中雨'},
                    {value: 2, name: '大雨'}
                ]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function echarts_33() {
        var myChart = echarts.init(document.getElementById('fb3'));
        option = {
            title: {
                text: '风向分布',
                left: 'center',
                textStyle: {
                    color: '#fff',
                    fontSize: '16'
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                top: '70%',
                itemWidth: 10,
                itemHeight: 10,
                data: ['东风', '西风', '南风', '北风', '无风'],
                textStyle: {
                    color: 'rgba(255,255,255,.5)',
                    fontSize: '12',
                }
            },
            series: [{
                name: '风向分布',
                type: 'pie',
                center: ['50%', '42%'],
                radius: ['40%', '60%'],
                color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab'],
                data: [
                    {value: 10, name: '东风'},
                    {value: 8, name: '西风'},
                    {value: 6, name: '南风'},
                    {value: 4, name: '北风'},
                    {value: 3, name: '无风'}
                ]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

})

		
		
		


		









