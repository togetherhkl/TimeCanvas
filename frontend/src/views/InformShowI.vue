<template>
    <div class="InterestingeventContainer">
        <el-row class="tac">
            <el-col :span="4">
                <el-menu class="scroll-container" default-active="2" @open="handleOpen" @close="handleClose">
                    <el-sub-menu index="1">
                        <template #title>
                            <el-icon>
                                <HomeFilled />
                            </el-icon>
                            <span>事件名称</span>
                        </template>
                        <el-input v-model="keyword" placeholder="请输入名称">
                            <template #suffix>
                                <el-icon style="cursor: pointer;" @click="search">
                                    <Search />
                                </el-icon>
                            </template>
                        </el-input>
                        <el-menu-item :index="`1-${index + 1}`" v-for="(item, index) in nameList" :key="index"
                            @click="selectEvent(item)">
                            {{ item.name }}
                            <el-tooltip content="编辑" palcement="top">
                                <el-icon class="update-icon" @click.stop="update(item)">
                                    <Edit />
                                </el-icon>
                            </el-tooltip>
                            <el-tooltip content="删除" palcement="top">
                                <el-icon class="delete-icon" @click.stop="confirmDelete(item)">
                                    <CloseBold />
                                </el-icon>
                            </el-tooltip>
                        </el-menu-item>
                    </el-sub-menu>
                    <el-sub-menu index="2"><template #title>
                            <el-icon>
                                <Menu />
                            </el-icon>
                            <span>管理</span>
                        </template>
                        <el-menu-item index="2-1" @click="CreateIPage">添加信息</el-menu-item>
                        <el-menu-item index="2-2" @click="getData">数据可视化</el-menu-item>
                    </el-sub-menu>
                </el-menu>
            </el-col>
            <el-col :span="20" class="right-content">
                <InformationI :selectedEvent="selectedEvent" />
                <Picture :selectedEvent="selectedEvent" />
                <Video :selectedEvent="selectedEvent" />
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { ElMessage, ElMessageBox } from 'element-plus';
const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
}

import { ref, onMounted } from 'vue';
import InformationI from '../components/InformationI.vue';
import Picture from '../components/Carousel/Picture.vue';
import Video from '../components/Carousel/Video.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
export default {
    components: {
        InformationI,
        Picture,
        Video,
    },
    methods: {
        // 添加信息
        CreateIPage() {
            /* 获取路由stage的值 */
            const lastRoute = this.$router.currentRoute.value.query.stage;
            this.$router.push({ path: '/interestingevents/createinterestingevent', query: { type: lastRoute } });
        },
        getData() {
            ElMessageBox.alert('数据可视化功能暂未开放', '提示', {
                confirmButtonText: '确定',
                type: 'warning'
            });
        },
        // 删除事件
        confirmDelete(item) {
            ElMessageBox.confirm(`确定删除 ${item.name} 吗？`, '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(async () => {
                const loadingInstance = ElLoading.service({ fullscreen: true });
                const tempEvent = this.selectedEvent;
                console.log('tempEvent:', tempEvent);
                const video_specifc_event = tempEvent.id;
                let video_album_type = ''; let video_album = '';
                let promises = [];//存放删除视频的promise
                const vpath = tempEvent.event_album_path;
                const [album_type, album] = vpath.split('/');
                axios.get('/albumtype').then(response => {
                    video_album_type = response.data.find(item => item.albumtype_name === album_type).id;
                    return axios.get('/album', { params: { album_type_id: video_album_type } });
                }).then(response => {
                    video_album = response.data.find(item => item.album_name === album).id;
                    return axios.get('/video', { params: { video_album_type: video_album_type, video_album: video_album, video_specifc_event: video_specifc_event } });
                }).then(response => {
                    const videoIds = response.data.map(item => item.id);
                    console.log('videoIds:', videoIds);
                    for (let i = 0; i < videoIds.length; i++) {
                        console.log('video_id:', videoIds[i]);
                        promises.push(axios.delete('/video', { params: { video_id: videoIds[i] } }));
                    }
                }).catch(error => { console.error('响应失败', error) });
                //删除图片
                const lastRoute = this.$router.currentRoute.value.query.stage;//获取路由stage的值
                let path = "/apps/TimeGallery/趣事录/" + lastRoute + "/" + item.name;
                let filepath = []
                path = path.replace(/'/g, '"') // 把单引号替换成双引号
                filepath.push(path)
                promises = [axios.delete('/interestingevent/', { params: { id: item.id } }),
                axios.delete("/baidufile/deletefile", { data: filepath }),
                ];
                const response = await Promise.all(promises);
                if (response.every(res => res.status === 200)) {
                    loadingInstance.close();
                    ElMessageBox.alert(`删除 ${item.name}成功`, '提示', {
                        confirmButtonText: '确定',
                        type: 'success'
                    }).then(() => {
                        this.$router.go(0);//刷新页面
                    });
                } else {
                    loadingInstance.close();
                    ElMessage.error(`删除 ${item.name}失败`);
                    return;//结束函数
                }
            }).catch(() => { console.log('取消删除'); });
        },
        // 编辑事件
        update(item) {
            this.$router.push({
                path: '/interestingevents/updateinterestingevent',
                query: { id: item.id, name: item.name, type: item.event_album_name }
            });
            console.log('update:', item);
        }
    },
    setup() {
        const EventsData = ref(null);// 事件数据
        const selectedEvent = ref(null);// 选中的事件
        const nameList = ref(null);// 事件名称列表
        const searchnamelist = ref(null);// 搜索事件名称列表
        const router = useRouter(); // 获取路由实例
        const keyword = ref('');// 搜索关键字
        onMounted(async () => {
            try {
                axios.get('/interestingevent', { params: { event_album_name: router.currentRoute.value.query.stage } }).then(response => {
                    EventsData.value = response.data;
                    nameList.value = EventsData.value.map(event => ({ name: event.event_name, id: event.id, event_album_name: event.event_album_name }));
                    if (nameList.value.length > 0) {
                        selectedEvent.value = EventsData.value[0];
                        const first = selectedEvent.value.event_name;
                        selectedEvent.value = EventsData.value.find(event => event.event_name === first);
                        selectedEvent.value.event_album_path = "趣事录/" + router.currentRoute.value.query.stage;
                    } else {
                        ElMessageBox.alert('没有匹配到事件的信息！,请到‘管理-添加信息’处添加事件信息', '提示', {
                            confirmButtonText: '确定',
                            type: 'warning'
                        });
                    }
                });
            } catch (error) {
                console.error('匹配失败:', error);
            }
        });
        const search = async () => {
            try {
                const response = await axios.get('/interestingevent', { params: { event_album_name: router.currentRoute.value.query.stage } }); // 替换为实际用于搜索事件名称的端点
                EventsData.value = response.data;// 获取事件列表数据
                searchnamelist.value = response.data.map(event => ({ name: event.event_name, id: event.id }));
                const searchResults = searchnamelist.value.filter(event => {
                    return event.name.includes(keyword.value);
                });
                nameList.value = searchResults; // 假设这里是更新左侧列表的变量名
            } catch (error) {
                ElMessage.error('搜索失败');
                console.error('搜索失败：', error);
            }
        };
        const selectEvent = (item) => {
            const stage = router.currentRoute.value.query.stage;
            if (nameList.value.length > 0) {
                selectedEvent.value = EventsData.value[0];
                selectedEvent.value = EventsData.value.find(event => event.event_name === item.name);
                selectedEvent.value.event_album_path = "趣事录/" + stage;
            }
        };
        return {
            selectedEvent,
            EventsData,
            nameList,
            searchnamelist,
            search,
            keyword,
            handleClose,
            handleOpen,
            selectEvent,
        };
    },
}
</script>
<style scoped>
.InterestingeventContainer {
    height: 100vh;
}

.scroll-container {
    height: calc(100vh - 40px);
    /* 计算容器高度为屏幕高度减去标题的高度 */
    overflow-y: auto;
    /* 垂直滚动条 */
}

.el-menu-item {
    cursor: pointer;
}

.el-menu-item:hover {
    border-radius: 5px;
    border: 1px solid #409EFF;
}

.update-icon,
.delete-icon {
    cursor: pointer;
    color: red;
    /* 使图标到最右侧 */
    float: right;
    margin-left: 20px;
}

.right-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
    overflow-y: auto;
    /* 垂直滚动条 */
    max-height: 100vh;
    scrollbar-width: thin;
    scrollbar-color: transparent transparent;
}

.right-content::-webkit-scrollbar {
    width: 5px;
    height: 5px;
}

.right-content::-webkit-scrollbar-thumb {
    background-color: #ccc;
    border-radius: 10px;
}

picture {
    height: 100px;
    width: 100px;
    background-color: #ccc;
}

video {
    margin-top: 20px;
}
</style>