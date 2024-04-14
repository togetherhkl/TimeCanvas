<template>
    <div class="add-classmates">
        <div class="add-card">
            <el-page-header @back="onBack">
                <div class="title">{{ name }}@{{ type }}时光卡片</div>
                <form>
                    <div class="layout">
                        <div class="name">
                            <label for="name">姓名:</label>
                            <input type="text" id="name" v-model="formData.name" required>
                        </div>
                        <div class="nickname">
                            <label for="nickname">昵称:</label>
                            <input type="text" id="nickname" v-model="formData.nickname" required>
                        </div>
                        <div class="avatar">
                            <!-- <label for="classmates_avatar_name">头像</label>
                            <input type="file" id="classmates_avatar_name" accept="image/*"
                                @change="handleAvatarChange">
                            <img v-if="avatarPreview" :src="avatarPreview" alt="Avatar Preview"
                                style="max-width: 200px; max-height: 200px;"> -->
                        </div>
                        <div class="birthday">
                            <label for="birthday">生日:</label>
                            <input type="date" id="birthday" v-model="formData.birthday" required>
                        </div>
                        <div class="constellation">
                            <label for="constellation">星座:</label>
                            <select style="width: 65%;" id="constellation" v-model="formData.constellation" required>
                                <option value="白羊座">白羊座</option>
                                <option value="金牛座">金牛座</option>
                                <option value="双子座">双子座</option>
                                <option value="巨蟹座">巨蟹座</option>
                                <option value="狮子座">狮子座</option>
                                <option value="处女座">处女座</option>
                                <option value="天秤座">天秤座</option>
                                <option value="天蝎座">天蝎座</option>
                                <option value="射手座">射手座</option>
                                <option value="摩羯座">摩羯座</option>
                                <option value="水瓶座">水瓶座</option>
                                <option value="双鱼座">双鱼座</option>
                            </select>
                        </div>
                        <div class="qq">
                            <label for="qq">QQ:</label>
                            <input type="text" id="qq_number" v-model="formData.qq_number" required>
                        </div>
                        <div class="wx">
                            <label for="wx_number">微信:</label>
                            <input type="text" id="wx_number" v-model="formData.wx_number" required>
                        </div>
                        <div class="phone">
                            <label for="phone">手机号:</label>
                            <input type="text" id="phone_number" v-model="formData.phone_number" required>
                        </div>
                        <div class="email">
                            <label for="email">邮箱:</label>
                            <input type="email" id="email" v-model="formData.email" required>
                        </div>

                    </div>
                    <div class="hometown">
                        <label for="hometown">家乡:</label>
                        <el-cascader v-model="selectedOptions" :options="options" @change="handleAreaChange"
                            placeholder="请选择省份和市区"> </el-cascader>
                        <el-input v-model="formData.hometown" placeholder="请手动填写详细地址" required></el-input>
                    </div>
                    <div class="layout-off">
                        <div class="hobby">
                            <label for="hobby">爱好:</label>
                            <textarea type="text" id="hobby" v-model="formData.hobby" required></textarea>
                        </div>
                        <div class="mengxiang">
                            <label for="dream">梦想:</label>
                            <textarea id="dream" v-model="formData.dream" required></textarea>
                        </div>
                        <div class="biyejiyu" @mouseup="showPopup">
                            <label for="graduation_message">毕业寄语:</label>
                            <div class="gmtext" v-html="markdownToHtml"></div>
                            <!-- <textarea id="graduation_message" v-model="formData.graduation_message" required></textarea> -->
                        </div>
                    </div>
                    <div class="button">
                        <button type="submit" @click="submitForm">确认</button>
                        <button type="reset" @click="resetForm">重置</button>
                    </div>
                </form>
            </el-page-header>
        </div>
    </div>
    <el-dialog v-model="dialogVisible" title="可AI生成的毕业寄语" width="90%"
        style="background-image: linear-gradient(to right top, #4db2d8, #2bbad5, #00c0cd, #02c6c0, #32cbae);"
        :before-close="handleClose">
        <GMDialog @update-vditortext="updateVditorText" />
    </el-dialog>
</template>

<script>
import { ElCascader,ElMessageBox } from 'element-plus';
import { regionData, codeToText } from 'element-china-area-data';
import axios from 'axios';
import GMDialog from './GMDialog.vue';
import { marked, options } from 'marked';//markdown解析器
export default {
    data() {
        return {
            selectedOptions: [],//级联选择器
            options: regionData,//级联选择器数据
            formData: {
                classmates_album_name: '',
                classmates_avatar_name: '',
                name: '',
                nickname: '',
                birthday: '',
                hometown: '',
                qq_number: '',
                wx_number: '',
                phone_number: '',
                email: '',
                constellation: '',
                hobby: '',
                dream: '',
                graduation_message: '',
            },
            avatarPreview: '',//头像预览
            name: '',//主题姓名
            type: '',//主题类型
            id: '',//主题id
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
            return marked(this.formData.graduation_message);
        },
    },
    watch: {
        '$route.query.name': {
            immediate: true,
            handler(newVal) {
                this.name = newVal;
                console.log('watch里name', this.name);
            },
        },
        '$route.query.type': {
            immediate: true,
            handler(newVal) {
                this.type = newVal;
                console.log('watch里type', this.type);
            },
        },
        '$route.query.id': {
            immediate: true,
            handler(newVal) {
                this.id = newVal;
                console.log('watch里id', this.id);
            },
        },
    },
    methods: {
        handleAvatarChange(event) {
            this.formData.classmates_avatar_name = event.target.files[0];
            this.avatarPreview = URL.createObjectURL(event.target.files[0]);
        },
        handleAreaChange(value) {
            if (value[0] != null && value[1] != null && value[2] != null) {
                const str = codeToText[value[0]] + '/' + codeToText[value[1]] + '/' + codeToText[value[2]];
                console.log('str:', str);
                this.formData.hometown = str + '/ ';
            }
            console.log('value:', value, 'hometown:', this.formData.hometown);
        },
        validatePhoneNumber() {
            if (this.formData.phone_number.length !== 11) {
                ElMessageBox.alert('电话号码必须是11位数', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
                return false;
            }
            return true;
        },
        validateQQNumber() {
            const qqRegex = /^[1-9][0-9]{8,9}$/;
            if (!qqRegex.test(this.formData.qq_number)) {
                ElMessageBox.alert('QQ号必须是9到10位数字', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
                return false;
            }
            return true;
        },
        submitForm() {
            const isPhoneValid = this.validatePhoneNumber();
            const isQQValid = this.validateQQNumber();
            if (isPhoneValid && isQQValid) {
                this.$emit('formSubmit', this.formData);
            } else {
                ElMessageBox.alert('请检查输入的电话号码或者QQ号', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
            }
        },
        resetForm() {
            // 重置表单数据
            this.$emit('formReset', this.resetForm);
            this.formData = {
                classmates_album_name: '',
                classmates_avatar_name: '',
                name: '',
                nickname: '',
                birthday: '',
                hometown: '',
                qq_number: '',
                wx_number: '',
                phone_number: '',
                email: '',
                constellation: '',
                hobby: '',
                dream: '',
                graduation_message: ''
            };
        },
        onBack() {
            this.$router.push({ path: '/同学录/informshow', query: { stage: this.type } });
        },
        //弹窗
        showPopup() {
            this.dialogVisible = true;
        },
        handleClose(done) {
            this.$confirm('确认完成毕业寄语吗？')
                .then(_ => {
                    done();
                })
                .catch(_ => { });
        },
        updateVditorText(newText) {
            this.formData.graduation_message = newText;//更新毕业寄语
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
            axios.get(`/classmate/${this.$route.query.type}`)
                .then(response => {
                    // 处理成功响应
                    const tempdata = response.data.classmates;
                    const matchedData = tempdata.find(item => item.id == this.id);
                    this.formData.classmates_album_name = matchedData.classmates_album_name;
                    this.formData.classmates_avatar_name = matchedData.classmates_avatar_name;
                    this.formData.name = matchedData.name;
                    this.formData.nickname = matchedData.nickname;
                    this.formData.birthday = new Date(matchedData.birthday).toISOString().slice(0, 10);
                    this.formData.hometown = matchedData.hometown;
                    this.formData.qq_number = matchedData.qq_number;
                    this.formData.wx_number = matchedData.wx_number;
                    this.formData.phone_number = matchedData.phone_number;
                    this.formData.email = matchedData.email;
                    this.formData.constellation = matchedData.constellation;
                    this.formData.hobby = matchedData.hobby;
                    this.formData.dream = matchedData.dream;
                    this.formData.graduation_message = matchedData.graduation_message;
                }).catch(error => {
                    console.error('响应失败！', error);
                });
        } else {
            this.formData.classmates_album_name = this.$route.query.type;
        }
    },
};
</script>

<style scoped>
.add-classmates {
    height: calc(100vh - 60px);
    width: 100%;
    overflow-y: auto;
}

.title {
    text-align: center;
    margin-bottom: 20px;
    font-size: 42px;
}

.layout {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 20px;
}

.layout-off {
    margin-top: 20px;
    display: grid;
    grid-template-rows: 1fr 1fr auto;
    grid-gap: 20px;
}

.avatar {
    grid-row: span 5;
}

.hobby textarea,
.mengxiang textarea,
.biyejiyu textarea {
    width: 100%;
    height: 100px;
    font-size: 16px;
}

.gmtext {
    width: 100%;
    min-height: 100px;
    height: auto;
    font-size: 16px;
}

.add-card {
    width: 70%;
    margin: 0 auto;
    padding: 20px;
    background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.hometown {
    width: 600px;
    display: grid;
    grid-template-columns: auto 1fr 1fr;
}

.form-row {
    display: flex;
    justify-content: space-between;
}

.add-card form div {
    margin-bottom: 10px;
}

.add-card form div label {
    display: inline-block;
    width: 70px;
}

.add-card form div input {
    font-size: 16px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.add-card form div select {
    font-size: 16px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.add-card form div textarea,
.gmtext {
    font-size: 16px;
    padding: 5px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.add-card form button {
    width: 100px;
    padding: 10px;
    margin: 10px;
    border: none;
    border-radius: 5px;
    background-color: #c88dee;
    color: #fff;
    font-size: 16px;
    cursor: pointer;
}

.add-card form button:active {
    background-color: #b3a5fa;
}

.add-card form button:hover {
    background-color: #a6b8fc;
}

.button {
    display: flex;
    justify-content: center;
}
</style>