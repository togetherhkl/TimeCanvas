<template>
    <div class="filelist">
        <div class="flex">
            <el-cascader filterable v-model="filePath" :options="options" placeholder="请选择要管理的视频文件夹"
                @change="cascaderChange" />
            <el-button type="primary" @click="uploadButoon" style="float:right">
                上传视频<el-icon class="el-icon--right">
                    <Upload />
                </el-icon>
            </el-button>
        </div>
        <el-table :data="tableData" stripe table-layout="auto">
            <el-table-column prop="video_nickname" label="视频名称" />
            <el-table-column prop="video_date" label="创建时间" />
            <el-table-column prop="video_size" label="视频大小" />
            <el-table-column column-key="operate" label="相关操作">
                <template #default="scope">
                    <el-row class="mb-4">
                        <el-button type="primary" @click="getDownload(scope.row.video_nickname, scope.row.video_name)">
                            <el-icon>
                                <Download />
                            </el-icon>
                            下载
                        </el-button>
                        <el-button type="primary" @click="getStream(scope.row.video_name)">
                            <el-icon>
                                <VideoPlay />
                            </el-icon>
                            浏览器播放
                        </el-button>
                        <el-popconfirm title="确定要删除吗?" @confirm="deleteItem(scope.row.id)">
                            <template #reference>
                                <el-button type="danger" :icon="Delete" plain round>删除视频</el-button>
                            </template>
                        </el-popconfirm>
                    </el-row>
                </template>
            </el-table-column>
        </el-table>
        <el-drawer v-model="drawer">
            <template #header>
                <h4>上传文件</h4>
            </template>
            <template #default>
                <el-upload drag action="/video" accept="video/*" :multiple="true" :auto-upload="false" :on-change="onChangeFile">
                    <el-icon class="el-icon--upload">
                        <upload-filled />
                    </el-icon>
                    <div class="el-upload__text">
                        拖动到此处或 <em>点击上传</em>
                    </div>
                </el-upload>
            </template>
            <template #footer>
                <div style="flex: auto">
                    <el-button type="primary" @click="onUpload">上传</el-button>
                </div>
            </template>
        </el-drawer>
    </div>
    <el-dialog v-model="dialogOverflowVisible" title="视频播放" width="600" draggable overflow>
        <div>
            <video :src="videoUrl" width="500px" controls="controls"></video>
        </div>
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogOverflowVisible = false">关闭</el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script>
import axios from "axios";
import { reactive, onMounted, defineComponent, toRefs, ref, computed } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { HomeFilled, Back, Upload, Delete, Sunny, Moon, User, Star } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { ElLoading } from 'element-plus'
import { useDark } from '@vueuse/core'
import { options } from "marked";

export default defineComponent({
    setup() {
        const isDark = useDark()
        const router = useRouter()
        const drawer = ref(false)
        const filePath = ref("")
        const uploadFile = ref(null)
        const dialogOverflowVisible = ref(false)
        const videoUrl = ref("")
        const state = reactive({
            tableData: [],
            options: [],
            fileList: []
        });
        const fetchData = async () => {
            const loadingInstance = ElLoading.service({ fullscreen: true })
            //加载级联选择器内容
            try {
                let options = await axios.get("/albumcascade");
                state.options = options.data;
                ElMessage({
                    message: '加载成功,选择第三层中的具体事件，管理视频数据！',
                    type: 'success',
                });
            } catch (err) {
                ElMessage.error('请求出错了: ' + err.message + ", " + (err.response ? err.response.data : ""))
            }
            loadingInstance.close();
        };
        const getDownload = (video_nickname,video_name) => {
            window.open("http://localhost:8000/videodownload/"+video_name+"?video_nickname=" + video_nickname);
        }
        //获取视频流
        const getStream = (video_name) => {
            dialogOverflowVisible.value = true;
            videoUrl.value = "http://localhost:8000/videostream/" + video_name;
        }
        onMounted(() => {
            fetchData();
        });
        const onUpload = async () => {
            const loadingInstance = ElLoading.service({ fullscreen: true })
            try {
                let formdata = new FormData();
                //把uploadFile存储的files数组放入formdata
                for (let file of uploadFile.value) {
                    formdata.append('files', file.raw);
                }
                formdata.append('video_album_type', parseInt(filePath.value[0]))
                formdata.append('video_album', parseInt(filePath.value[1]))
                formdata.append('video_specifc_event', parseInt(filePath.value[2]))
                await axios.post("/video", formdata, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(res => {
                    console.log(res)
                }).catch(err => {
                    console.log(err)
                });
                ElMessage({
                    message: '上传成功',
                    type: 'success',
                });
            } catch (err) {
                ElMessage.error('请求出错了: ' + err.message + ", " + (err.response ? err.response.data : ""))
            }
            drawer.value = false;
            loadingInstance.close();
        }
        const onChangeFile = (file, files) => {
            uploadFile.value = files
        }
        const deleteItem = async (id) => {
            console.log(id)
            // const loadingInstance = ElLoading.service({ fullscreen: true })
            // try {
            //     await axios.delete("/delete?path=" + curPath.value + name);
            //     ElMessage({
            //         message: '删除成功',
            //         type: 'success',
            //     });
            //     router.go(0);
            // } catch (err) {
            //     ElMessage.error('请求出错了: ' + err.message + ", " + (err.response ? err.response.data : ""))
            // }
            // loadingInstance.close();
        };
        //视频上传按钮
        const uploadButoon = () => {
            //判断级联选择器是否选择了文件夹
            if (filePath.value == "") {
                ElMessage.error("请选择文件夹");
                return;
            }
            if (filePath.value.length < 3) {
                ElMessage.error("请选择第三层中的具体事件，如果没有请创建具体事件");
                return;
            }
            // console.log(filePath.value)
            drawer.value = true;
        }
        //级联选择器改变事件
        const cascaderChange = (value) => {
            if (value.length < 3) {
                ElMessage.warning("请选择第三层中的具体事件，才有视频数据！")
                state.tableData = [];
                return;
            }
            let data = {
                video_album_type: value[0],
                video_album: value[1],
                video_specifc_event: value[2]
            }
            axios.get("/video", {
                params: data
            }).then(res => {
                state.tableData = res.data;
                if (res.data.length == 0)
                    ElMessage.warning("当前事件没有视频文件哦，点击上传视频按钮上传视频吧！")
                // console.log(res.data)
            }).catch(err => {
                ElMessage.error('请求出错了: ' + err.message + ", " + (err.response ? err.response.data : ""))
            });
        }
        return {
            ...toRefs(state),
            onUpload,
            getDownload,
            onChangeFile,
            deleteItem,
            uploadButoon,
            getStream,
            cascaderChange,
            videoUrl,
            filePath,
            drawer,
            router,
            dialogOverflowVisible,
            HomeFilled,
            Back,
            Upload,
            Delete,
            isDark,
            Sunny, Moon, User, Star,
        }
    }
})
</script>

<style>
.filelist {
    margin-top: 20px;
    margin-left: 10px;
    margin-right: 10px;
}
</style>