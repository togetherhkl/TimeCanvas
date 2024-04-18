<template>
    <div class="add-interestingevent">
        <div class="add-card">
            <div class="title">{{ name }}@{{ type }}时光卡片</div>
            <div class="form">
                <div class="event_name">
                    <label for="event_name">事件名称</label>
                    <input type="text" v-model="formData.event_name" placeholder="请输入事件名称" />
                </div>
                <div class="event_date">
                    <label for="event_date">事件日期</label>
                    <input type="date" v-model="formData.event_date" />
                </div>
                <div class="event_participant">
                    <label for="event_participant">事件参与者</label>
                    <textarea v-model="formData.event_participant" placeholder="请输入事件参与者" />
                </div>
                <div class="event_description" @mouseup="showPopup">
                    <label for="event_description">事件描述</label>
                    <div class="edtext" v-html="markdownToHtml"></div>
                    <!-- <textarea v-model="formData.event_description" placeholder="请输入事件描述"></textarea> -->
                </div>
                <div class="button">
                    <button type="submit" @click="submitForm">确认</button>
                    <button type="reset" @click="resetForm">重置</button>
                </div>
            </div>
        </div>
    </div>
    <el-dialog v-model="dialogVisible" title="可AI生成的事件描述" width="90%"
        style="background-image: linear-gradient(to right top, #4db2d8, #2bbad5, #00c0cd, #02c6c0, #32cbae);"
        :before-close="handleClose">
        <GMDialog @update-vditortext="updateVditorText" />
    </el-dialog>
</template>

<script>
import axios from 'axios';
import { ElMessageBox,ElCascader } from 'element-plus';
import { marked, options } from 'marked';//markdown解析器
import GMDialog from './GMDialog.vue';
export default {
    data() {
        return {
            formData: {
                event_name: '',
                event_date: '',
                event_description: '',
                event_participant: '',
                event_album_image: '',
                event_album_name: '',
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
        ElCascader,
    },
    emits: ['formSubmit', 'formReset'],
    computed: {
        markdownToHtml() {
            return marked(this.formData.event_description);
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
            this.$confirm('确认完成事件描述吗？')
                .then(_ => {
                    done();
                })
                .catch(_ => { });
        },
        updateVditorText(newText) {
            this.formData.event_description = newText;//更新毕业寄语
        },
        submitForm() {
            this.$emit('formSubmit', this.formData);
        },
        resetForm() {
            // 重置表单数据
            this.$emit('formReset', this.resetForm);
            this.formData = {
                event_name: '',
                event_date: '',
                event_description: '',
                event_participant: '',
            };
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
            axios.get('/interestingevent', { params: { event_album_name: this.$route.query.type } })
                .then(response => {
                    // 处理成功响应
                    const tempdata = response.data;
                    const matchedData = tempdata.find(item => item.id == this.id);
                    this.formData = matchedData;
                    console.log('响应成功！', response);
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
.add-interestingevent {
    height: calc(100vh - 70px);
    width: 100%;
    overflow-y: auto;
}

.add-card {
    width: 70%;
    margin: 0 auto;
    padding: 20px;
    /* display: grid;
    grid-template-rows: repeat(4, 1fr);
    gap: 20px;
    align-items: center; */
    background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.title {
    font-size: 42px;
    margin-bottom: 10px;
    text-align: center;
}
.form .event_name,
.form .event_date,
.form .event_participant,
.form .event_description {
    display: flex;
    align-items: center;
    margin: 40px 150px;
}

.add-card label {
    display: inline-block;
    width: 100px;
}

.add-card input,
.add-card textarea,
.add-card .edtext {
    width: 100%;
    font-size: 16px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.add-card input {
    width: 200px;
}
.add-card textarea, .edtext{
    width: 100%;
    height: auto;
    min-height: 100px;
    font-size: 16px;
}
.add-card textarea {
    height: 100px;
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