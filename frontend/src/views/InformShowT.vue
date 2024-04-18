<template>
    <div class="travelContainer">
        <el-row class="tac">
            <el-col :span="4">
                <el-menu class="scroll-container" default-active="2" @open="handleOpen" @close="handleClose">
                    <el-sub-menu index="1">
                        <template #title>
                            <el-icon><HomeFilled /></el-icon>
                            <span>旅游主题</span>
                        </template>
                        <el-input v-model="keyword" placeholder="请输入旅游主题">
                            <template #suffix>
                                <el-icon style="cursor: pointer;" @click="search">
                                    <Search />
                                </el-icon>
                            </template>
                        </el-input>
                        <el-menu-item :index="`1-${index+1}`" v-for="(item, index) in nameList" :key="index"
                            @click="selectTravel(item)">
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
                <InformationT :selectedTravel="selectedTravel"/>
                <Picture :selectedTravel="selectedTravel" />
                <Video />
            </el-col>
        </el-row>
    </div>
    <el-dialog v-model="dialogVisible" width="70%">
        <Map />
    </el-dialog>
</template>

<script>
import { ElMessageBox } from 'element-plus';
const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
}

import { ref, onMounted } from 'vue';
import InformationT from '../components/InformationT.vue';
import Picture from '../components/Carousel/Picture.vue';
import Video from '../components/Carousel/Video.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import Map from '../components/Map.vue';
export default {
    data() {
        return {
            dialogVisible:false,
        }
    },
    components: {
        InformationT,
        Picture,
        Video,
        Map,
    },
    methods: {
        // 添加信息
        CreateIPage(){
            /* 获取路由stage的值 */
            const lastRoute = this.$router.currentRoute.value.query.stage;
            this.$router.push({ path: '/travels/createtravel',query: { type:lastRoute } });
        },
        getData() {
            this.dialogVisible=true;
        },
        // 删除同学
        confirmDelete(item) {
        ElMessageBox.confirm(`确定删除 ${item.name} 吗？`, '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        }).then(() => {
            // Handle deletion logic here
            console.log('id:',item.id);
            axios.delete('/travel/',{params:{id:item.id}}).then(
                response=>{
                    if(response.status==200){
                        console.log(`删除 ${item.name}成功`);
                        this.$router.go(0);//刷新页面
                    }else{
                        console.log('删除失败');
                    }
                }
            ).catch(error=>{
                console.error('删除失败:',error);
            });
        }).catch(() => {
            // Cancelled deletion
            console.log('取消删除');
        });
    },
    // 编辑同学
    update(item){
        this.$router.push({ 
            path: '/travels/updatetravel',
            query: { id:item.id,name:item.name,type:item.travel_album_name }
         });
        console.log('update:',item);
    }
    },
    setup() {
        const TravelsData = ref(null);// travels数据
        const selectedTravel = ref(null);// 选中的travels
        const nameList = ref(null);// travels名称列表
        const searchnamelist = ref(null);// 搜索列表
        const router = useRouter(); // 获取路由实例
        const keyword = ref('');// 搜索关键字
        onMounted(async () => {
            try {
                axios.get('/travel',{params:{travel_album_name:router.currentRoute.value.query.stage}}).then(response => {
                    TravelsData.value = response.data;
                    nameList.value = TravelsData.value.map(travel => ({name:travel.travel_theme,id:travel.id,travel_album_name:travel.travel_album_name}));
                    if(nameList.value.length>0){
                        selectedTravel.value = TravelsData.value[0];
                        const first=selectedTravel.value.travel_theme;
                        selectTravel.value = TravelsData.value.find(travel => travel.travel_theme === first);
                        selectTravel.value.travel_album_path="旅游志/"+router.currentRoute.value.query.stage;
                    }else{
                        ElMessageBox.alert('没有匹配到旅游的信息！,请到‘管理-添加信息’处添加旅游信息', '提示', {
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
                const response = await axios.get('/travel',{params:{travel_album_name:router.currentRoute.value.query.stage}}); // 替换为实际用于搜索事件名称的端点
                TravelsData.value = response.data;// 获取旅游列表数据
                searchnamelist.value = response.data.map(travel => ({ name: travel.travel_theme, id: travel.id }));// 获取旅游名称列表
                const searchResults = searchnamelist.value.filter(travel => {
                    return travel.name.includes(keyword.value);
                });
                nameList.value = searchResults; // 假设这里是更新左侧列表的变量名
            } catch (error) {
                console.error('搜索失败：', error);
            }
        };
        const selectTravel = (item) => {
            const stage = router.currentRoute.value.query.stage;
            if(nameList.value.length>0){
                selectedTravel.value = TravelsData.value[0];
                selectedTravel.value = TravelsData.value.find(travel => travel.travel_theme === item.name);
                selectedTravel.value.travel_album_path="旅游志/"+stage;
            }
        };
        return {
            selectedTravel,
            TravelsData,
            nameList,
            searchnamelist,
            search,
            keyword,
            handleClose,
            handleOpen,
            selectTravel,
        };
    },
}
</script>
<style scoped>
.travelContainer {
    height: 100vh;
}
.scroll-container {
    height: calc(100vh - 40px); /* 计算容器高度为屏幕高度减去标题的高度 */
    overflow-y: auto; /* 垂直滚动条 */
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
    overflow-y: auto; /* 垂直滚动条 */
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