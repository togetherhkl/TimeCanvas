<template>
    <div class="video">
    <el-carousel :interval="interval" arrow="hover">
        <el-carousel-item v-for="item in videos" :key="item">
            <!-- <video controls src="../../assets/1.mp4"></video> -->
            <video controls :src=item.src style="width: 100%;height: 100%;object-fit: contain;"  @play="handlePlay" @pause="handlePause"></video>
            <!-- <h3 text="2xl" justify="center">{{ item }}</h3> -->
        </el-carousel-item>
    </el-carousel>
    </div>
</template>
<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
    setup() {
        const videos = ref([]); // 视频列表
        const carousel=ref(null);
        const interval=ref(5000);
        onMounted(async () => {
            try {
                // const response = await axios.get('/api/videos');
                // videos.value = response.data;
                videos.value=[
                    {id:1,src:"https://upos-sz-mirror08c.bilivideo.com/upgcxcode/50/40/1475574050/1475574050-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1711956202&gen=playurlv2&os=08cbv&oi=0&trid=d7b12fe8b98b4b9693a33d56f4f6dd38T&mid=1700658102&platform=html5&upsig=d97e96d89219693ac90f16dfd32dd782&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&bw=57531&orderid=0,1&buvid=&build=0&mobi_app=&f=T_0_0&logo=80000000" },
                    {id:2,src:"https://www.runoob.com/try/demo_source/movie.mp4"},
                    {id:3,src:"https://www.runoob.com/try/demo_source/movie.mp4"},
                ]
            } catch (error) {
                console.error(error);
            }
        });
        const handlePlay=()=>{
            interval.value=0;
        };
        const handlePause=()=>{
            interval.value=5000;
        };
        return {
            videos,
            interval,
            handlePause,
            handlePlay,
        };
    }
};
</script>
<style>
.video {
    margin-top: 80px;
    width: 60%;
    margin-bottom: 50px;
}
/* 视频轮播图样式 */
.el-carousel__item:nth-child(2n) {
    /* background-color: #99a9bf; */
    background-color: black;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>