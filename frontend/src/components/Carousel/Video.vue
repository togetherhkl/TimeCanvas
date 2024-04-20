<template>
    <div class="video">
        <el-carousel :interval="interval" arrow="hover">
            <el-carousel-item v-for="item in videos" :key="item">
                <!-- <video controls src="../../assets/1.mp4"></video> -->
                <video controls :src=item style="width: 100%;height: 100%;object-fit: fill;" @play="handlePlay"
                    @pause="handlePause"></video>
                <!-- <h3 text="2xl" justify="center">{{ item }}</h3> -->
            </el-carousel-item>
        </el-carousel>
    </div>
</template>
<script>
import { ref, watch } from 'vue';
import axios from 'axios';
import { ElNotification } from 'element-plus';

export default {
    props: {
        selectedClassmate: {
            type: Object,
            default: null
        },
        selectedEvent: {
            type: Object,
            default: null
        },
        selectedTravel: {
            type: Object,
            default: null
        },
    },
    setup(props) {
        const videos = ref([]); // 视频列表
        const carousel = ref(null);
        const interval = ref(5000);
        watch(() => props.selectedClassmate, (newVal) => {
            if (newVal) {
                const video_specifc_event = newVal.id;
                let video_album_type = '';
                let video_album = '';
                const path = newVal.classmates_album_path;
                const [album_type, album] = path.split('/');
                axios.get('/albumtype').then(response => {
                    video_album_type = response.data.find(item => item.albumtype_name === album_type).id;
                    return axios.get('/album', { params: { album_type_id: video_album_type } });
                }).then(response => {
                    video_album = response.data.find(item => item.album_name === album).id;
                    return axios.get('/video', { params: { video_album_type: video_album_type, video_album: video_album, video_specifc_event: video_specifc_event } });
                }).then(response => {
                    const videoNames = response.data.map(item => item.video_name);
                    videos.value = videoNames.map(name => `http://localhost:8000/videostream/${name}`);
                    if (videoNames.length == 0) {
                        ElNotification({
                            title: '提示',
                            dangerouslyUseHTMLString: true,
                            message: '<strong><i>没有匹配到同学的视频信息！请到视频管理处添加</i></strong>',
                        });
                    }
                }).catch(error => { console.error('响应失败', error) });
            } else {
                console.log('没有匹配到同学的视频信息！');
            };
        });
        watch(() => props.selectedEvent, (newVal) => {
            if (newVal) {
                const video_specifc_event = newVal.id;
                let video_album_type = '';
                let video_album = '';
                const path = newVal.event_album_path;
                const [album_type, album] = path.split('/');
                axios.get('/albumtype').then(response => {
                    video_album_type = response.data.find(item => item.albumtype_name === album_type).id;
                    return axios.get('/album', { params: { album_type_id: video_album_type } });
                }).then(response => {
                    video_album = response.data.find(item => item.album_name === album).id;
                    return axios.get('/video', { params: { video_album_type: video_album_type, video_album: video_album, video_specifc_event: video_specifc_event } });
                }).then(response => {
                    const videoNames = response.data.map(item => item.video_name);
                    videos.value = videoNames.map(name => `http://localhost:8000/videostream/${name}`);
                    if (videos.value.length == 0) {
                        ElNotification({
                            title: '提示',
                            dangerouslyUseHTMLString: true,
                            message: '<strong><i>没有匹配到活动的视频信息！请到视频管理处添加</i></strong>',
                        });
                    }
                }).catch(error => { console.error('响应失败', error) });
            } else {
                console.log('没有匹配到活动的视频信息！');
            };

        });
        watch(() => props.selectedTravel, (newVal) => {
            if (newVal) {
                const video_specifc_event = newVal.id;
                let video_album_type = '';
                let video_album = '';
                const path = newVal.travel_album_path;
                const [album_type, album] = path.split('/');
                axios.get('/albumtype').then(response => {
                    video_album_type = response.data.find(item => item.albumtype_name === album_type).id;
                    return axios.get('/album', { params: { album_type_id: video_album_type } });
                }).then(response => {
                    video_album = response.data.find(item => item.album_name === album).id;
                    return axios.get('/video', { params: { video_album_type: video_album_type, video_album: video_album, video_specifc_event: video_specifc_event } });
                }).then(response => {
                    const videoNames = response.data.map(item => item.video_name);
                    videos.value = videoNames.map(name => `http://localhost:8000/videostream/${name}`);
                    if (videos.value.length == 0) {
                        ElNotification({
                            title: '提示',
                            dangerouslyUseHTMLString: true,
                            message: '<strong><i>没有匹配到旅游的视频信息！请到视频管理处添加</i></strong>',
                        });
                    }
                }).catch(error => { console.error('响应失败', error) });
            } else {
                console.log('没有匹配到旅游的视频信息！');
            };
        });
        const handlePlay = () => {
            interval.value = 0;
        };
        const handlePause = () => {
            interval.value = 5000;
        };
        return { videos, interval, handlePause, handlePlay, };
    }
};
</script>
<style scoped>
.video {
    margin-top: 80px;
    width: 70%;
    margin-bottom: 50px;
}

.el-carousel__item:nth-child(2n) {
    background-color: black;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

::v-deep .el-carousel__container {
    min-height: 450px;
}
</style>