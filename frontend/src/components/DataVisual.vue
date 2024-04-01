<template>
    <div class="layout">
        <div id="chart" style="width: 100%; height: 500px; float: left;"></div>
        <div id="chinamap" style="width: 100%; height: 500px; float: left;"></div>
        <div id="ageChart" style="width: 100%; height: 500px; float: left;"></div>
        <div id="wordCloud" style="width: 100%; height: 500px; float: left;"></div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';
import china from 'echarts/map/china.json';
import 'echarts-wordcloud';
echarts.registerMap('china', china);

export default {
    setup() {
        const chartData = ref(null);

        onMounted(() => {
            fetchChartData().then(data => {
                const myChart = echarts.init(document.getElementById('chart'));
                myChart.setOption({
                    title: {
                        text: '同学录地区分布柱状图'
                    },
                    tooltip: {},
                    xAxis: {
                        data: data.categories
                    },
                    yAxis: {},
                    series: [
                        {
                            name: '人数',
                            type: 'bar',
                            data: data.series
                        }
                    ]
                });

                const mapChart = echarts.init(document.getElementById('chinamap'));
                mapChart.setOption({
                    title: {
                        text: '同学录地区分布地图'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{b}<br/>{c}人'
                    },
                    visualMap: {
                        min: 0,
                        max: 100,
                        left: 'left',
                        top: 'bottom',
                        text: ['高', '低'],
                        calculable: true
                    },
                    series: [
                        {
                            name: '人数',
                            type: 'map',
                            mapType: 'china',
                            label: {
                                show: true
                            },
                            data: data.mapData
                        }
                    ]
                });

                const ageChart = echarts.init(document.getElementById('ageChart'));
                ageChart.setOption({
                    title: {
                        text: '同学录年龄分布条形图'
                    },
                    tooltip: {},
                    xAxis: {
                        type: 'category',
                        data: ['0-10', '11-20', '21-30', '31-40', '41-50', '50+']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name: '人数',
                            type: 'bar',
                            data: [10, 30, 50, 70, 20, 5] // 假设这里是年龄分布数据
                        }
                    ]
                });

                const wordCloud = echarts.init(document.getElementById('wordCloud'));
                wordCloud.setOption({
                    title: {
                        text: '兴趣爱好词云图'
                    },
                    series: [
                        {
                            type: 'wordCloud',
                            shape: 'circle',
                            gridSize: 20,
                            sizeRange: [20, 80],
                            rotationRange: [-45, 45],
                            textStyle: {
                                normal: {
                                    color: function() {
                                        return 'rgb(' + [
                                            Math.round(Math.random() * 255),
                                            Math.round(Math.random() * 255),
                                            Math.round(Math.random() * 255)
                                        ].join(',') + ')';
                                    }
                                }
                            },
                            data: [
                                { name: '篮球', value: 100 },
                                { name: '足球', value: 80 },
                                { name: '阅读', value: 60 },
                                { name: '旅行', value: 50 },
                                { name: '编程', value: 40 },
                                { name: '音乐', value: 30 },
                                { name: '美食', value: 20 }
                            ] // 假设这里是兴趣爱好数据
                        }
                    ]
                });
            });
        });

        function fetchChartData() {
            return new Promise(resolve => {
                setTimeout(() => {
                    const data = {
                        categories: ['北京', '上海', '广州', '深圳', '成都', '杭州'],
                        series: [50, 30, 40, 35, 45, 55],
                        mapData: [
                            { name: '北京', value: 50 },
                            { name: '上海', value: 30 },
                            { name: '广州', value: 40 },
                            { name: '深圳', value: 35 },
                            { name: '成都', value: 45 },
                            { name: '杭州', value: 55 }
                        ]
                    };
                    resolve(data);
                }, 1000);
            });
        }

        return {
            chartData
        };
    }
}
</script>

<style scoped>
.layout {
    width: 100%;
    height: 100%;
    overflow-y: auto;
    /* background-color: red; */
}
</style>
