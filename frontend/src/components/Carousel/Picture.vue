<template>
    <div class="picture">
        <el-carousel :interval="5000" type="card" arrow="hover">
            <el-carousel-item v-for="item in pictures" :key="item">
                <el-image style="width: 100%; height: 100%;" :src=item fit="fill" :crossorigin="null" />
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
        const pictures = ref([]);//图片列表
        const backdata = ref([]);//储存后端传过来的数据：id和name
        watch(() => props.selectedClassmate, (newVal) => {
            if (newVal) {
                backdata.value = { id: newVal.id, name: newVal.name };
                axios.get('/albumfiles', { params: { folder_name: newVal.classmates_album_path + '/' + newVal.name + '/pictures' } })
                    .then(response => {
                        pictures.value = response.data;
                        if (pictures.value.length == 0) {
                            ElNotification({
                                title: '提示',
                                dangerouslyUseHTMLString: true,
                                message: '<strong><i>没有匹配到同学的照片信息!请到到“照片管理”下添加</i></strong>',
                            });
                        }
                    }).catch(error => { console.error('响应失败！', error); });
            } else {
                console.log('没有匹配到同学的照片信息！');
            };
        });
        watch(() => props.selectedEvent, (newVal) => {
            if (newVal) {
                backdata.value = { id: newVal.id, name: newVal.event_name };
                axios.get('/albumfiles', { params: { folder_name: newVal.event_album_path + '/' + newVal.event_name + '/pictures' } })
                    .then(response => {
                        pictures.value = response.data;
                        if (pictures.value.length == 0) {
                            ElNotification({
                                title: '提示',
                                dangerouslyUseHTMLString: true,
                                message: '<strong><i>没有匹配到活动的照片信息!请到到“照片管理”下添加</i></strong>',
                            });
                        }
                    }).catch(error => { console.error('响应失败！', error); });
            } else {
                console.log('没有匹配到活动的照片信息！');
            };
        });
        watch(() => props.selectedTravel, (newVal) => {
            if (newVal) {
                backdata.value = { id: newVal.id, name: newVal.travel_theme };
                axios.get('/albumfiles', { params: { folder_name: newVal.travel_album_path + '/' + newVal.travel_theme + '/pictures' } })
                    .then(response => {
                        pictures.value = response.data;
                        if (pictures.value.length == 0) {
                            ElNotification({
                                title: '提示',
                                dangerouslyUseHTMLString: true,
                                message: '<strong><i>没有匹配到旅游的照片信息!请到到“照片管理”下添加</i></strong>',
                            });
                        }
                    }).catch(error => { console.error('响应失败！', error); });
            } else {
                console.log('没有匹配到旅游的照片信息！');
            };
        });
        return { pictures, backdata };
    },
};

</script>
<style scoped>
.picture {
    margin-top: 40px;
    width: 100%;
    height: auto;
    padding: 10px;
    align-items: center;
    justify-content: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

:deep(.el-carousel__container) {
    min-height: 350px;
}

</style>