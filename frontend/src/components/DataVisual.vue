<template>
    <div class="layout">
        <h1 class="centered-and-bold">{{stage}}数据可视化</h1>
        <div id="chart" class="chartdiv" ></div>
        <div id="chinamap" class="chartdiv" ></div>
        <div id="ageChart" class="chartdiv" ></div>
        <div id="wordCloud" class="chartdiv" ></div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router'; // 用于获取路由参数
import * as echarts from 'echarts';
import china from 'echarts/map/china.json';
import 'echarts-wordcloud';
import { ElMessage } from 'element-plus';
import axios from 'axios';
echarts.registerMap('china', china);



export default {
    setup() {
        const router = useRouter();
        const chartData = ref(null);
        const stage =ref(router.currentRoute.value.query.stage);
        onMounted(() => {

            fetchChartData().then(data => {
                console.log('stage:',stage);
                const myChart = echarts.init(document.getElementById('chart'));
                myChart.setOption({
                    title: {
                        text: '同学录地区分布柱状图'
                    },
                    tooltip: {},
                    xAxis: {
                        data: data.categories
                        // data: ['北京', '上海', '广州', '深圳', '成都', '杭州'] // 假设这里是地区分布数据
                    },
                    yAxis: {},
                    series: [
                        {
                            name: '人数',
                            type: 'bar',
                            data: data.series
                            // data: [50, 30, 40, 35, 45, 55] // 假设这里是地区分布数据
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
                axios.get('/classmate_statiscts/age_bar', { params: { stage: router.currentRoute.value.query.stage } })
                    .then(response => {
                        const ageChart = echarts.init(document.getElementById('ageChart'));
                        ageChart.setOption({
                            title: {
                                text: '同学录年龄分布条形图'
                            },
                            tooltip: {},
                            xAxis: {
                                type: 'category',
                                data: response.data.categories
                            },
                            yAxis: {
                                type: 'value'
                            },
                            series: [
                                {
                                    name: '人数',
                                    type: 'bar',
                                    data: response.data.series
                                }
                            ]
                        });

                    })
                    .catch(error => {
                        ElMessage.error('获取数据失败');
                    })

                axios.get('/classmate_statiscts/interest_wordcloud', { params: { stage: router.currentRoute.value.query.stage } })
                    .then(response => {
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
                                            color: function () {
                                                return 'rgb(' + [
                                                    Math.round(Math.random() * 255),
                                                    Math.round(Math.random() * 255),
                                                    Math.round(Math.random() * 255)
                                                ].join(',') + ')';
                                            }
                                        }
                                    },
                                    data: response.data.wordcloud

                                    // data: [
                                    //     { name: '篮球', value: 100 },
                                    //     { name: '足球', value: 80 },
                                    //     { name: '阅读', value: 60 },
                                    //     { name: '旅行', value: 50 },
                                    //     { name: '编程', value: 40 },
                                    //     { name: '音乐', value: 30 },
                                    //     { name: '美食', value: 20 }
                                    // ] // 假设这里是兴趣爱好数据
                                }
                            ]
                        });
                    })
                    .catch(error => {
                        ElMessage.error('获取数据失败');
                    });
            });
        });

        function fetchChartData() {
            return new Promise(resolve => {
                axios.get('/classmate_statiscts/location_bar', { params: { stage: router.currentRoute.value.query.stage } })
                    .then(response => {
                        console.log(response.data);
                        resolve(response.data);
                    })
                    .catch(error => {
                        ElMessage.error('获取数据失败');
                    })
                // setTimeout(() => {
                //     const data = {
                //         categories: ['北京', '上海', '广州', '深圳', '成都', '杭州'],
                //         series: [50, 30, 40, 35, 45, 55],
                //         mapData: [
                //             { name: '北京', value: 50 },
                //             { name: '上海', value: 30 },
                //             { name: '广州', value: 40 },
                //             { name: '深圳', value: 35 },
                //             { name: '成都', value: 45 },
                //             { name: '杭州', value: 55 }
                //         ]
                //     };
                //     resolve(data);
                // }, 1000);
            });
        }

        return {
            chartData,
            stage
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
.centered-and-bold {
    font-weight: bold; /* 加粗文本 */
    text-align: center; /* 居中文本 */
}
.chartdiv{
    width: 100%; 
    height: 500px; 
    float: left;
    border: 1px inset #40688a; /* 添加边框 */
    margin: 20px 0; /* 添加上下距离 */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* 添加阴影 */
}

</style>
