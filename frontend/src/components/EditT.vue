<template>
    <div class="add-travel">
        <div class="add-card">
            <div class="title">{{ name }}@{{ type }}时光卡片</div>
            <div class="form">
                <div class="travel_theme">
                    <label for="travel_theme">旅游主题</label>
                    <input type="text" v-model="formData.travel_theme" />
                </div>
                <div class="travel_date">
                    <label for="travel_date">旅游日期</label>
                    <input type="date" v-model="formData.travel_date" />
                </div>
                <div class="travel_place">
                    <label for="travel_place">旅游地点</label>
                        <el-cascader class="selectedcontain"  v-model="selectedOptions" :options="options" @change="handleAreaChange"
                            placeholder="请选择省份和市区"> </el-cascader>
                        <el-input v-model="formData.travel_place" placeholder="请手动填写详细地址" required></el-input>
                </div>
                <div class="travel_participant">
                    <label for="travel_participant">旅游参与者</label>
                    <textarea v-model="formData.travel_participant"/>
                </div>
                <div class="travel_description" @mouseup="showPopup">
                    <label for="travel_description">旅游描述</label>
                    <div class="tdtext" v-html="markdownToHtml"></div>
                    <!-- <textarea v-model="formData.travel_description"></textarea> -->
                </div>
                <div class="button">
                    <button type="submit" @click="submitForm">确认</button>
                    <button type="reset" @click="resetForm">取消并返回</button>
                </div>
            </div>
        </div>
    </div>
    <el-dialog v-model="dialogVisible" title="可AI生成的旅游描述" width="90%"
        style="background-image: linear-gradient(to right top, #4db2d8, #2bbad5, #00c0cd, #02c6c0, #32cbae);"
        :before-close="handleClose">
        <GMDialog @update-vditortext="updateVditorText" />
    </el-dialog>
</template>

<script>
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
import { regionData, codeToText } from 'element-china-area-data';
import { marked, options } from 'marked';//markdown解析器
import GMDialog from './GMDialog.vue';
export default {
    data() {
        return {
            selectedOptions:[],
            options: regionData,//省市区数据
            formData: {
                travel_theme: '',//旅游主题
                travel_date: '',//旅游日期
                travel_description: '',//旅游描述
                travel_participant: '',//旅游参与者
                travel_place: '',//旅游具体地点
                travel_province:'',///旅游省份
                travel_album_name:'',//旅游相册类型
            },
            name: '',//主题姓名
            type: '',//主题类型
            id: '',//主题id
            editor: null,
            dialogVisible: false, //弹窗
        };
    },
    components: {
        GMDialog,
    },
    emits: ['formSubmit'],
    computed: {
        markdownToHtml() {
            return marked(this.formData.travel_description);
        },
    },
    watch: {
        '$route.query.name': {
            immediate: true,
            handler(newVal) {
                this.name = newVal;
            },
        },
        '$route.query.type': {
            immediate: true,
            handler(newVal) {
                this.type = newVal;
            },
        },
        '$route.query.id': {
            immediate: true,
            handler(newVal) {
                this.id = newVal;
            },
        },
    },
    methods: {
        showPopup() {
            this.dialogVisible = true;
        },
        handleClose(done) {
            this.$confirm('确认完成旅游描述吗？')
                .then(_ => {
                    done();
                }).catch(_ => { });
        },
        updateVditorText(newText) {
            this.formData.travel_description = newText;//更新毕业寄语
        },
        handleAreaChange(value) {
            if (value[0] != null && value[1] != null && value[2] != null) {
                const str = codeToText[value[0]] + '/' + codeToText[value[1]] + '/' + codeToText[value[2]];
                this.formData.travel_province=str+'/';
            }
        },
        submitForm() {
            this.$emit('formSubmit', this.formData);
        },
        resetForm() {
            const type = this.$router.currentRoute.value.query.type;
            this.$router.push({ path: '/travels/informshow', query: { stage: type } });
        },
    },
    props: {
        fetchData: {
            type: Boolean,
            default: true,
        },
    },
    mounted() {
        if (this.fetchData) {
            axios.get('travel', { params: { travel_album_name: this.$route.query.type } })
                .then(response => {
                    // 处理成功响应
                    const tempdata = response.data;
                    const matchedData = tempdata.find(item => item.id == this.id);
                    this.formData = matchedData;
                    console.log(this.formData);
                    let date =new Date(matchedData.travel_date);
                    date.setHours(date.getHours() + 8);//时区问题
                    this.formData.travel_date = date.toISOString().slice(0, 10);
                }).catch(error => {
                    console.error('响应失败！', error);
                });
        } else {
            console.log('不需要获取数据');
        }
    },
};
</script>

<style scoped>
.add-travel {
    height: calc(100vh - 70px);
    width: 100%;
    overflow-y: auto;
}
.add-card {
    width: 70%;
    margin: 0 auto;
    padding: 20px;
    background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.title {
    font-size: 42px;
    margin-bottom: 10px;
    text-align: center;
}
.form .travel_theme,
.form .travel_date,
.form .travel_place,
.form .travel_participant,
.form .travel_description{
    display: flex;
    align-items: center;
    margin: 40px 100px 20px 100px ;
}
.form div .el-cascader{
    width: 400px;
}
.form div .el-input{
    width: 400px;
}
.add-card label {
    display: inline-block;
    width: 100px;
    margin: 0px;
    white-space: nowrap;
}
.add-card input,
.add-card textarea,.tdtext {
    font-size: 16px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}
.add-card textarea, .tdtext{
    width: 100%;
    height: auto;
    min-height: 100px;
    font-size: 16px;
}
.add-card button {
    width: 100px;
    height: 40px;
    margin: 0 20px;
    border: none;
    border-radius: 5px;
    background: #c88dee;
    color: #fff;
    font-size: 16px;
    cursor: pointer;
}

.add-card button:hover {
    background: #a6b8fc;
}

.add-card button:active {
    background: #b3a5fa;
}

.button {
    display: flex;
    justify-content: center;
}
</style>