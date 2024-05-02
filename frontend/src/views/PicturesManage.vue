<template>
    <div class="filelist">
        <div class="flex">
            <el-cascader filterable :options="options" placeholder="请选择要管理的照片文件夹" :props="{ checkStrictly: true }"
                ref="cascaderArr" @change="cascaderChange" />
            <el-button type="primary" @click="uploadButoon" style="float:right">
                {{ uploadmessage }}<el-icon class="el-icon--right">
                    <Upload />
                </el-icon>
            </el-button>
            <div class="imagesdiv">
                <div v-for="(item, index) in imagesinfo" class="imageshow">
                    <el-image style="width: 330px; height: 200px" :src="item.url3" :zoom-rate="1.2" :max-scale="7"
                        :min-scale="0.2" :preview-src-list="imagesrclist" :initial-index=index fit="cover"
                        :crossorigin="null" />
                    <div style="padding: 5px; border: 1px solid #ccc;">
                        <span>{{ item.server_filename }}({{ item.size }})</span>
                        <el-popconfirm title="确定要删除吗?" @confirm="deleteItem(item.path,index)">
                            <template #reference>
                                <el-button type="danger" :icon="Delete" plain round></el-button>
                            </template>
                        </el-popconfirm>
                    </div>

                </div>
            </div>
        </div>
    </div>
    <el-drawer v-model="drawer">
        <template #header>
            <h4>上传文件</h4>
        </template>
        <template #default>
            <el-upload drag action="/picture" accept="image/*" :multiple="imagemultiple" :auto-upload="false"
                :on-change="onChangeFile">

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
        const drawer = ref(false)
        const uploadFile = ref(null)
        const imagemultiple = ref(true)
        const uploadmessage = ref("上传照片")
        const imagesfilepath = ref("")
        const cascaderArr = ref(null);
        const state = reactive({
            options: [],
            fileList: [],
            imagesinfo: [],
            imagesrclist: []
        });
        const fetchData = async () => {
            const loadingInstance = ElLoading.service({ fullscreen: true })
            //加载级联选择器内容
            try {
                let options = await axios.get("/albumcascade");
                state.options = options.data;
                ElMessage({
                    message: '加载成功,请选择文件，管理图片数据！',
                    type: 'success',
                });
            } catch (err) {
                ElMessage.error('请求出错了: ' + err.message + ", " + (err.response ? err.response.data : ""))
            }
            loadingInstance.close();
        };
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
                // console.log(imagesfilepath.value)
                formdata.append('folder_name', imagesfilepath.value)
                await axios.post("/baidufile/uploadimage", formdata, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(res => {
                    console.log(res)
                    imagesfilepath.value = ""
                }).catch(err => {
                    console.log(err)
                    return;
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
        const deleteItem = async (path,index) => {
            // console.log(path)
            let filepath = []
            path = path.replace(/'/g, '"')//把单引号替换成双引号
            filepath.push(path)
            // console.log(filepath)
            const loadingInstance = ElLoading.service({ fullscreen: true })
            try {
                await axios.delete("/baidufile/deletefile", {
                    data: filepath
                }).then(res => {
                    // console.log(res)
                    if (res.data.errno == 2) {
                        ElMessage.error("百度网盘删除服务器已暂停，请在百度网盘上删除")
                        return;
                    }
                    else {
                        state.imagesinfo.splice(index, 1)
                        ElMessage({
                            message: '删除成功',
                            type: 'success',
                        });
                    }
                }).catch(err => {
                    console.log(err)
                    return;
                });

            } catch (err) {
                ElMessage.error('请求出错了: ' + err.message + ", " + (err.response ? err.response.data : ""))
            }
            loadingInstance.close();
        };
        //照片上传按钮
        const uploadButoon = () => {
            //判断级联选择器是否选择了文件夹
            if (imagesfilepath.value == "") {
                ElMessage.error("请选择文件夹");
                return;
            }
            // console.log(filePath.value)
            drawer.value = true;
        }
        //级联选择器改变事件
        const cascaderChange = (value) => {
            if (value.length == 1) {
                uploadmessage.value = "更改相册类型封面"
                imagemultiple.value = false;
                state.imagesinfo = [];
            }
            if (value.length == 2) {
                uploadmessage.value = "更改相册封面"
                imagemultiple.value = false;
                state.imagesinfo = [];
            }
            if (value.length == 3) {
                uploadmessage.value = "上传具体事件照片"
                imagemultiple.value = true;
                state.imagesinfo = [];
            }
            const checkedNode = cascaderArr.value.getCheckedNodes();
            // console.log(checkedNode[0].data.label);  //获取当前点击节点的label值
            // console.log(checkedNode[0].pathLabels);  //获取由label组成的数组
            //把数据拼接路劲字符
            imagesfilepath.value = checkedNode[0].pathLabels.join("/");
            // console.log(imagesfilepath)
            if (value.length == 3) {
                imagesfilepath.value = imagesfilepath.value + "/pictures"
            }
            axios.get("/baidufile/imageslist", {
                params: {
                    folder_name: imagesfilepath.value
                }
            }).then(res => {
                // console.log(res.data)
                state.imagesinfo = res.data;
                if (res.data.length == 0)
                    ElMessage.warning("当前文件没有照片哦，请上传对应的照片把！")
                //把图片信息的url放入数组,预览方式会出现跨域问题，未能解决
                for (let item of state.imagesinfo) {
                    state.imagesrclist.push(item.url3)
                }
                // console.log(state.imagesinfo)
                // console.log(state.imagesrclist)
            }).catch(err => {
                ElMessage.error('请求出错了: ' + err.message + ", " + (err.response ? err.response.data : ""))
            });
        }
        return {
            ...toRefs(state),
            onUpload,
            onChangeFile,
            deleteItem,
            uploadButoon,
            cascaderChange,

            imagesfilepath,
            cascaderArr,
            imagemultiple,
            drawer,
            uploadmessage,
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

.imageshow {
    margin-top: 10px;
    margin-left: 10px;
    display: flex;
    flex-direction: column;
    font-family: 'Arial', sans-serif;
    /* 使用Arial字体，如果无法找到Arial字体，则使用sans-serif字体 */
    font-size: 16px;
    /* 设置字体大小为16像素 */
    color: #333;
    /* 设置字体颜色为深灰色 */
    line-height: 1.5;
    /* 设置行高为1.5，这可以使文字更易于阅读 */
    text-align: justify;
    /* 设置文字对齐方式为两端对齐，这可以使段落看起来更整齐 */
    /* 添加阴影 */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.imagesdiv {
    padding: 20px;
    display: flex;
    flex-wrap: wrap;
}
</style>