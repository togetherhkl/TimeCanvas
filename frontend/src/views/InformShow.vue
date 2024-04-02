<template>
    <div class="primary">
        <el-row class="tac">
            <el-col :span="3">
                <el-menu class="scroll-container" default-active="2" @open="handleOpen" @close="handleClose">
                    <el-sub-menu index="1">
                        <template #title>
                            <el-icon>
                                <User />
                            </el-icon>
                            <span>姓名</span>
                        </template>
                        <el-input v-model="keyword" placeholder="请输入姓名">
                <template #suffix>
                    <el-icon style="cursor: pointer;" @click="search">
                        <Search />
                    </el-icon>
                </template></el-input>
                        <el-menu-item index="1-1" v-for="(name, index) in nameList" :key="index" :index="index"
                            :class="{ 'is-active': selectedClassmate && selectedClassmate.name === name }"
                            @click="selectedClassmate = classmatesData.find(classmate => classmate.name === name)">{{ name }}
                        </el-menu-item>

                    </el-sub-menu>
                    <el-sub-menu index="2"><template #title>
                            <el-icon><Plus /></el-icon>
                            <span>更多</span>
                        </template>
                        <el-menu-item index="2-1"  @click="getData">数据可视化</el-menu-item>
                        <el-menu-item index="2-2">item two</el-menu-item>
                    </el-sub-menu>
                </el-menu>
            </el-col>
            <el-col :span="21" class="right-content">
                <Information :selectedClassmate="selectedClassmate" />
                <GraduationMessage :selectedClassmate="selectedClassmate" />
                <Picture />
                <Video />
            </el-col>
        </el-row>
    </div>
</template>

<script>
import {
    Document,
    Menu as IconMenu,
    Plus,
    User,
    Setting,
} from '@element-plus/icons-vue'
import { ElMessageBox } from 'element-plus';
const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
}

import { ref, onMounted } from 'vue';
import Navigation from '../components/Navigation.vue';
import Information from '../components/Information.vue';
import GraduationMessage from '../components/GraduationMessage.vue';
import Picture from '../components/Carousel/Picture.vue';
import Video from '../components/Carousel/Video.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
export default {
    data() {
        return {
            keyword: '',
        }
    },
    components: {
        Navigation,
        Information,
        GraduationMessage,
        Picture,
        Video,
    },
    methods: {
        getData() {
            ElMessageBox.alert('数据可视化功能暂未开放', '提示', {
                confirmButtonText: '确定',
                type: 'warning'
            });
        },
    },
    setup() {
        /* const selectedIndex = ref(null);
        const nameList = ref(['张三', '李四', '王五', '赵六', '李四', '王五', '赵六', '李四', '王五', '赵六', '李四', '王五', '赵六', '李四', '王五', '赵六']);
        const longNameList = ref(Array.from({ length: 4 }, (_, index) => `姓名${index + 1}`));
        return {
            nameList,
            longNameList,
            selectedIndex,
        }; */
        const classmatesData = ref(null);
        const selectedClassmate = ref(null);
        const nameList = ref([]);
        const searchnamelist = ref([]);
        const router = useRouter();
        const keyword = ref('');
        let album;

        onMounted(async () => {
            try {
                /* 获取当前路径路由 */
                const currentRoute = router.currentRoute.value;
                console.log('当前路径路由:', currentRoute);
                /* 获取路由最后一个字段 */

                const lastRoute = router.currentRoute.value.query.stage;
                console.log('查询的具体相册:', lastRoute);

                // const albumResponse=await axios.get('/classmate/小学')
                // //console.log('albumresponse:',albumResponse);
                // album=albumResponse.data.classmates;
                // console.log('路由',album)

                const response = await axios.get(`/classmate/${lastRoute}`);
                console.log(response.data);
                classmatesData.value = response.data.classmates;
                nameList.value = response.data.classmates.map(classmate => classmate.name);
            } catch (error) {
                // console.log('获取数据失败:', error);
                console.error('匹配失败:', error);
            }
        });
        const search = async () => {
            try {
                const currentRoute = router.currentRoute.value;
                const lastRoute = currentRoute.path.split('/').pop();
                console.log('路由最后一个字段:', lastRoute);

                //const response = await axios.get(`/classmate/${lastRoute}`); // 替换为实际用于搜索姓名的端点
                const response = await axios.get('/classmate/senior'); 
                console.log('response:', response.data);

                classmatesData.value = response.data.classmates;
                searchnamelist.value = response.data.classmates.map(classmate => classmate.name);
                console.log('namelist:', searchnamelist.value);
                const searchResults = searchnamelist.value.filter(name => {
                    return name.includes(keyword.value);
                });
                nameList.value = searchResults; // 假设这里是更新左侧列表的变量名
            } catch (error) {
                console.error('搜索失败：', error);
            }
        };
        return {
            selectedClassmate,
            classmatesData,
            nameList,
            searchnamelist,
            search,
            keyword,
            handleClose,
            handleOpen,
        };
    },
}
</script>
<style scoped>
.primary {
    height: 100vh;
}

.el-menu-item:hover,
.el-menu-item.is-active {
    /* background-color: #409EFF; */
    border-radius: 5px;
    border: 1px solid #409EFF;
}

.scroll-container {
    height: calc(100vh - 40px);
    /* 计算容器高度为屏幕高度减去标题的高度 */
    overflow-y: auto;
    /* 垂直滚动条 */
}

.right-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    /* background-color: green; */
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