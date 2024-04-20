<template>
    <div class="layout">
        <h1 class="centered-and-bold">{{ stage }}数据可视化</h1>
        <div id="chart" class="chartdiv"></div>
        <Chinamap class="chartdiv" :apiEndpoint="apiEndpoint" :album="stage" />
        <div id="constellation" class="chartdiv"></div>
        <!-- <div id="ageChart" class="chartdiv"></div> -->
        <div id="wordCloud" class="chartdiv"></div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router'; // 用于获取路由参数
import * as echarts from 'echarts';
import 'echarts-wordcloud';
import { ElMessage } from 'element-plus';
import axios from 'axios';
import Chinamap from '../components/Map.vue'
export default {
    components: {
        Chinamap
    },
    setup() {
        const router = useRouter();
        const chartData = ref(null);
        const apiEndpoint = '/classmate_statiscts/location_bar';
        const stage = ref(router.currentRoute.value.query.stage);
        onMounted(() => {
            fetchChartData().then(data => {
                // console.log('stage:', stage);
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
                // 画年龄分布柱状图
                // axios.get('/classmate_statiscts/age_bar', { params: { stage: router.currentRoute.value.query.stage } })
                //     .then(response => {
                //         const ageChart = echarts.init(document.getElementById('ageChart'));
                //         ageChart.setOption({
                //             title: {
                //                 text: `同学录${stage1}年龄分布条形图`
                //             },
                //             tooltip: {},
                //             xAxis: {
                //                 type: 'category',
                //                 data: response.data.categories
                //             },
                //             yAxis: {
                //                 type: 'value'
                //             },
                //             series: [
                //                 {
                //                     name: '人数',
                //                     type: 'bar',
                //                     data: response.data.series
                //                 }
                //             ]
                //         });

                //     })
                //     .catch(error => {
                //         ElMessage.error('获取年龄数据失败');
                //     })
                // 画星座分布雷达图
                axios.get('/classmate_statiscts/constellation_radar', { params: { stage: router.currentRoute.value.query.stage } })
                    .then(response => {
                        const constellation = echarts.init(document.getElementById('constellation'));
                        constellation.setOption({
                            backgroundColor: '#020933', // 设置背景颜色为深蓝色，模拟星空
                            title: {
                                text: '同学星座人数分布雷达图',
                                textStyle: {
                                    color: '#fff' // 设置标题颜色为白色
                                }
                            },
                            tooltip: {},
                            radar: {
                                name: {
                                    textStyle: {
                                        color: '#fff' // 设置雷达图各个指示器名称的颜色为白色
                                    },
                                },
                                // indicator: [
                                //     { name: '白羊座', max: 100 },
                                //     { name: '金牛座', max: 100 },
                                //     { name: '双子座', max: 100 },
                                //     { name: '巨蟹座', max: 100 },
                                //     { name: '狮子座', max: 100 },
                                //     { name: '处女座', max: 100 },
                                //     { name: '天秤座', max: 100 },
                                //     { name: '天蝎座', max: 100 },
                                //     { name: '射手座', max: 100 },
                                //     { name: '摩羯座', max: 100 },
                                //     { name: '水瓶座', max: 100 },
                                //     { name: '双鱼座', max: 100 }
                                // ],
                                indicator: response.data.indicator,
                                splitArea: { show: false, },
                                axisLine: {
                                    lineStyle: {
                                        color: 'rgba(128, 128, 128, 0.5)' // 设置雷达图轴线的颜色，使其更加透明
                                    }
                                },
                                splitLine: {
                                    lineStyle: {
                                        color: 'rgba(128, 128, 128, 0.5)' // 设置雷达图分割线的颜色，使其更加透明
                                    }
                                }
                            },
                            series: [
                                {
                                    name: '星座人数',
                                    type: 'radar',
                                    lineStyle: {
                                        color: '#FF6A6A' // 设置雷达图线条的颜色为亮红色
                                    },
                                    data: [
                                        {//星座分布数据，第一个白羊座，第二个金牛座，以此类推
                                            // value: [80, 90, 70, 60, 80, 90, 70, 60, 80, 90, 70, 60],
                                            value: response.data.value,
                                        }
                                    ]
                                }
                            ]
                        });

                    })
                    .catch(error => {
                        ElMessage.error('获取星座数据失败');
                    });

                // 画兴趣爱好词云图
                axios.get('/classmate_statiscts/interest_wordcloud', { params: { stage: router.currentRoute.value.query.stage } })
                    .then(response => {
                        const wordCloud = echarts.init(document.getElementById('wordCloud'));
                        wordCloud.setOption({
                            title: {
                                text: '同学兴趣爱好词云图'
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
                        ElMessage.error('获取爱好数据失败');
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
            stage,
            apiEndpoint
        };
    }
}
</script>

<style scoped>
.layout {
    width: 100%;
    height: 100%;
    overflow-y: auto;
}

.centered-and-bold {
    font-weight: bold;
    /* 加粗文本 */
    text-align: center;
    /* 居中文本 */
}

.chartdiv {
    width: 100%;
    height: 500px;
    float: left;
    border: 1px inset #40688a;
    /* 添加边框 */
    margin: 20px 0;
    /* 添加上下距离 */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    /* 添加阴影 */
}
</style>
