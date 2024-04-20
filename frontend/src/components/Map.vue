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
import { ElMessage } from 'element-plus'
import axios from 'axios';
export default {
    props: {
        apiEndpoint: {
            type: String,
            required: true
        },
        album:{
            type:String,
            required:true
        }
    },
    setup(props) {
        const path=ref(useRouter().currentRoute.value.path);
        const parts=path.value.split('/');
        let stage=parts[parts.length-2];//获取路由倒数第二个
        //获取路由倒数第二个字段
        const chartData = ref(null);//图表数据
        onMounted(() => {
            fetchChartData().then(data => {
                // console.log("stage:",stage);
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
                axios.get(props.apiEndpoint,{params:{stage:props.album}}).then(response => {
                    // resolve(response.data);
                    console.log(response.data);
                    const names=response.data.categories
                    const values=response.data.series
                    let mapData=[];
                    for(let i=0;i<names.length;i++){
                        mapData.push({name:names[i],value:values[i]});
                    }
                    let data={
                        mapData:mapData
                    }
                    console.log("map:",data);
                    resolve(data);
                }).catch(error => {
                    ElMessage.error('请求出错了: ' + error.message + ", " + (error.response ? error.response.data : ""))
                });
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