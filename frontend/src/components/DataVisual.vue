<template>
    <div class="layout">
        <h1 class="centered-and-bold">{{ stage }}数据可视化</h1>
        <div id="chart" class="chartdiv"></div>
        <Chinamap class="chartdiv" :apiEndpoint="apiEndpoint" :album="stage" />
        <div id="constellation" class="chartdiv"></div>
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
                const myChart = echarts.init(document.getElementById('chart'));
                myChart.setOption({
                    title: { text: '同学录地区分布柱状图' },
                    tooltip: {},
                    xAxis: { data: data.categories },
                    yAxis: {},
                    series: [{ name: '人数', type: 'bar', data: data.series }]
                });
                // 画星座分布雷达图
                axios.get('/classmate_statiscts/constellation_radar', { params: { stage: router.currentRoute.value.query.stage } }).then(response => {
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
                            name: { textStyle: { color: '#fff' }, },// 设置雷达图指示器的字体颜色为白色
                            indicator: response.data.indicator,// 星座数据
                            splitArea: { show: false, },// 不显示雷达图背景区域
                            axisLine: { lineStyle: { color: 'rgba(128, 128, 128, 0.5)' }, },// 设置雷达图分割线的颜色，使其更加透明
                            splitLine: { lineStyle: { color: 'rgba(128, 128, 128, 0.5)' }, },// 设置雷达图背景线的颜色，使其更加透明
                        },
                        series: [
                            {
                                name: '星座人数', type: 'radar',
                                lineStyle: { color: '#FF6A6A' },// 设置线条颜色为红色
                                data: [{ value: response.data.value, }]// 星座人数数据
                            }
                        ]
                    });

                }).catch(error => { ElMessage.error('获取星座数据失败'); });

                // 画兴趣爱好词云图
                axios.get('/classmate_statiscts/interest_wordcloud', { params: { stage: router.currentRoute.value.query.stage } }).then(response => {
                    const wordCloud = echarts.init(document.getElementById('wordCloud'));
                    wordCloud.setOption({
                        title: { text: '同学兴趣爱好词云图' },
                        series: [
                            {
                                type: 'wordCloud', shape: 'circle', gridSize: 20,
                                sizeRange: [20, 80], rotationRange: [-45, 45],
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
                                data: response.data.wordcloud// 兴趣爱好数据
                            }
                        ]
                    });
                }).catch(error => { ElMessage.error('获取爱好数据失败'); });
            });
        });
        function fetchChartData() {
            return new Promise(resolve => {
                axios.get('/classmate_statiscts/location_bar', { params: { stage: router.currentRoute.value.query.stage } }).then(response => {
                    // console.log(response.data);
                    resolve(response.data);// 返回数据
                }).catch(error => { ElMessage.error('获取数据失败'); })
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
