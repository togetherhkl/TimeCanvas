<template>
    <div class="layout">
        <div id="chinamap" style="width: 100%; height: 500px; float: left;"></div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';
import china from '../assets/map/china.json';
echarts.registerMap('china', china);
import { useRouter } from 'vue-router';
export default {
    setup() {
        const path=ref(useRouter().currentRoute.value.path);
        const parts=path.value.split('/');
        let stage=parts[parts.length-2];//获取路由倒数第二个
        //获取路由倒数第二个字段
        const chartData = ref(null);//图表数据
        onMounted(() => {
            fetchChartData().then(data => {
                console.log("stage:",stage);
                if(stage=='classmates'){
                    stage='同学录';
                }else{
                    stage='旅游';
                }
                const mapChart = echarts.init(document.getElementById('chinamap'));
                // if(stage)
                mapChart.setOption({
                    title: {
                        text: `${stage}地区分布地图`
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
                                show: true,
                            },
                            data:data.mapData,
                        }
                    ]
                });
            });
        });
        function fetchChartData() {
            return new Promise(resolve => {
                setTimeout(() => {
                    const data = {
                        mapData: [
                            { name: '北京市', value: 50 },
                            { name: '上海市', value: 30 },
                            { name: '广州省', value: 40 },
                            { name: '四川省', value: 35 },
                            { name: '西藏自治区', value: 45 },
                            { name: '云南省', value: 55 }
                        ]
                    };
                    resolve(data);//返回数据
                }, 1000);
            });
        }
        return {
            chartData,
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
    text-align: center;
}
</style>