<template>
  <div class="add-layout">
    <div class="add-title">
      <h1>添加同学录信息</h1>
    </div>
    <div class="add">
      <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="150px" class="demo-ruleForm"
        :size="formSize" status-icon>
        <div class="type">
          <el-form-item label="同学录相册名称" prop="classmates_album_name">
            <el-radio-group v-model="ruleForm.classmates_album_name">
              <el-radio label="primary" >小学</el-radio>
              <el-radio label="junior" >初中</el-radio>
              <el-radio label="senior" >高中</el-radio>
              <el-radio label="university">大学</el-radio>
            </el-radio-group>
          </el-form-item>
        </div>
        <div class="name-image">
          <el-row :span="24">
            <el-col :span="8">
              <el-form-item label="姓名" prop="name">
                <el-input v-model="ruleForm.name" />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="昵称" prop="nickname">
                <el-input v-model="ruleForm.nickname" />
              </el-form-item>
            </el-col>
            <el-col :span="6">
              <el-form-item label="同学头像" prop="classmates_avatar_name">
                <el-input v-model="ruleForm.classmates_avatar_name" />
                
               <!--  <el-upload
    class="avatar-uploader"
   action="url"
    :show-file-list="false"
    :on-success="handleAvatarSuccess"
    :before-upload="beforeAvatarUpload"
  >
    <img v-if="imageUrl" :src="imageUrl" class="avatar" />
    <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
  </el-upload> -->
                <!-- <el-upload class="avatar-uploader" action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :show-file-list="false" :on-success="handleAvatarSuccess" :befor-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <el-icon v-else class="avatar-uploader-icon">
              <Plus />
            </el-icon>
          </el-upload> -->

              </el-form-item>
            </el-col>
          </el-row>
        </div>
        <div class="birthday-hometown">
          <el-row :span="24">
            <el-col :span="8">
              <el-form-item label="生日" required>
                  <el-form-item prop="birthday">
                    <el-date-picker v-model="ruleForm.birthday" type="date" label="Pick a date" format="YYYY/MM/DD"
        value-format="YYYY-MM-DD" style="width: 100%" />
                  </el-form-item>
              </el-form-item>
            </el-col>
            <el-row :span="8">
              <el-form-item label="家乡" prop="hometown">
                <el-input v-model="ruleForm.hometown" />
              </el-form-item>
            </el-row>
          </el-row>
        </div>
        <div class="hobby">
          <el-row :span="24">
          <el-form-item label="爱好" prop="hobby">
            <!-- <el-input v-model="ruleForm.hobby" /> -->
            <el-checkbox-group v-model="ruleForm.hobby">
              <el-checkbox label="篮球" name="type">篮球</el-checkbox>
              <el-checkbox label="羽毛球" name="type">羽毛球</el-checkbox>
              <el-checkbox label="足球" name="type">足球</el-checkbox>
              <el-checkbox label="跑步" name="type">跑步</el-checkbox>
              <el-checkbox label="聊天" name="type">聊天</el-checkbox>
            </el-checkbox-group>
            <el-col :span="16">
            <el-input  v-model="ruleForm.hobby"  placeholder="请输入其他爱好"></el-input>
            </el-col>
            <el-button @click="addnewHobby">添加爱好</el-button>
          </el-form-item>
          </el-row>
         <!--  <p>已选爱好：{{ ruleForm.hobby }}</p> -->
        </div>
        <div class="contact">
          <el-row :span="24">
            <el-col :span="8">
              <el-form-item label="QQ" prop="qq_number">
                <el-input v-model="ruleForm.qq_number" />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="微信" prop="wx_number">
                <el-input v-model="ruleForm.wx_number" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-row :span="24">
            <el-col :span="8">
              <el-form-item label="手机号" prop="phone_number">
                <el-input v-model="ruleForm.phone_number" />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="邮箱" prop="email">
                <el-input v-model="ruleForm.email" />
              </el-form-item>
            </el-col>
          </el-row>
        </div>
        <div class="xingzuo">
          <el-form-item label="星座" prop="constellation">
            <el-select v-model="ruleForm.constellation" placeholder="">
              <el-option label="白羊座" value="白羊座">
                <i class="iconfont icon-muyangzuo">白羊座</i>
              </el-option>
              <el-option label="金牛座" value="金牛座">
                <i class="iconfont icon-jinniuzuo">金牛座</i>
              </el-option>
              <el-option label="双子座" value="双子座">
                <i class="iconfont icon-shuangyuzuo">双子座</i>
              </el-option>
              <el-option label="巨蟹座" value="巨蟹座">
                <i class="iconfont icon-juxiezuo">巨蟹座</i>
              </el-option>
              <el-option label="狮子座" value="狮子座">
                <i class="iconfont icon-shizizuo">狮子座</i>
              </el-option>
              <el-option label="处女座" value="处女座">
                <i class="iconfont icon-chunvzuo">处女座</i>
              </el-option>
              <el-option label="天秤座" value="天秤座">
                <i class="iconfont icon-tianchengzuo">天秤座</i>
              </el-option>
              <el-option label="天蝎座" value="天蝎座">
                <i class="iconfont icon-tianhezuo">天蝎座</i>
              </el-option>
              <el-option label="射手座" value="射手座">
                <i class="iconfont icon-sheshouzuo">射手座</i>
              </el-option>
              <el-option label="摩羯座" value="摩羯座">
                <i class="iconfont icon-mojiezuo">摩羯座</i>
              </el-option>
              <el-option label="水瓶座" value="水瓶座">
                <i class="iconfont icon-shuipingzuo">水瓶座</i>
              </el-option>
              <el-option label="双鱼座" value="双鱼座">
                <i class="iconfont icon-muyangzuo">双鱼座</i>
              </el-option>
            </el-select>
          </el-form-item>
        </div>
        <div class="message">
          <el-form-item label="梦想" prop="dream">
            <el-input v-model="ruleForm.dream"/>
          </el-form-item>
          <el-form-item label="毕业寄语" prop="graduation_message">
            <el-input v-model="ruleForm.graduation_message" type="textarea" />
          </el-form-item>
        </div>
        <div class="bottom">
          <el-form-item>
            <el-button type="primary" @click="submitForm(ruleFormRef)">
              添加
            </el-button>
            <el-button @click="resetForm(ruleFormRef)">重置</el-button>
          </el-form-item>
        </div>
      </el-form>
    </div>
  </div>
</template>
<script setup lang="ts">
import { reactive, ref } from 'vue';
import type { FormInstance, FormRules } from 'element-plus';
import { ElForm, ElFormItem, ElCheckboxGroup, ElCheckbox, ElInput, ElButton } from 'element-plus';
import axios from 'axios';
const form = ref({
  hobby: [] as string[]
});
const newHobby = ref('');

const addnewHobby = () => {
  if (newHobby.value) {
    form.value.hobby.push(newHobby.value);
    newHobby.value = '';
  }
  console.log(ruleForm.hobby);
};

import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'

import type { UploadProps } from 'element-plus'

const imageUrl = ref('')

const handleAvatarSuccess: UploadProps['onSuccess'] = (
  response,
  uploadFile
) => {
  imageUrl.value = URL.createObjectURL(uploadFile.raw!)
}

const beforeAvatarUpload: UploadProps['beforeUpload'] = (rawFile) => {
  /* if (rawFile.type !== 'image/jpeg') {
    ElMessage.error('Avatar picture must be JPG format!')
    return false
  } else if (rawFile.size / 1024 / 1024 > 2) {
    ElMessage.error('Avatar picture size can not exceed 2MB!')
    return false
  } */
  return true
}

interface RuleForm {
  name: string,
  nickname: string,
  birthday: string,
  hometown: string,
  hobby: string[],
  qq_number: string,
  wx_number: string,
  phone_number: string,
  email: string,
  constellation: string,/* 星座 */
  dream: string,
  graduation_message: string,
  classmates_album_name: string,
  classmates_avatar_name: string,
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  classmates_album_name: '',
  classmates_avatar_name: '',
  name: '',
  nickname: '',
  birthday: '',
  hometown: '',
  hobby: [],
  qq_number: '',
  wx_number: '',
  phone_number: '',
  email: '',
  constellation: '',/* 星座 */
  dream: '',
  graduation_message: '',
})
//规则
const rules = reactive<FormRules<RuleForm>>({
  classmates_album_name: [
    { required: true, message: '请选择添加的同学录相册名称', trigger: 'blur' }
  ],
  classmates_avatar_name: [

  ],
  name: [
    { required: true, message: '请输入姓名', trigger: 'blur' },
    { min: 1, max: 20, message: '姓名过长！', trigger: 'blur' },
  ],
  birthday: [
    {
      type: 'date',
      required: true,
      message: '请输入生日',
      trigger: 'change',
    },
  ],
  qq_number:[
    {min:9,max:11,message:'QQ号输入有误',trigger:'blur'}
  ],
  phone_number:[
  {min:11,max:11,message:'手机号输入有误',trigger:'blur'}
  ],
  graduation_message: [
    { required: true, message: '请输入毕业寄语', trigger: 'blur' },
  ],
})
// 定义一个函数，用于将数据发送至数据库
const sendDataToDatabase = async (formData) => {
  try {
    console.log("数据")
    console.log(typeof formData);
    console.log(formData.birthday);
    console.log(formData);
    axios.post('/classmate/',formData).then(function (response) {
    console.log(response.data);
  })
  } catch (error) {
    console.error('发送数据至数据库时出错:', error);
  }
};
//提交表单
const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      // console.log('submit!');
      console.log(ruleForm);
      console.log(ruleForm.classmates_album_name);

      // sendDataToDatabase(ruleForm);
    } else {
      console.log('error submit!', fields)
    }
  })
}
//重置表单
const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}
</script>

<style scoped>
.add-layout {
  width: 100%;
  height: 100vh;
  overflow: hidden;
  display: grid;
  grid-template-rows: 80px 1fr;
  background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
}

.add-layout .add-title {
  overflow: hidden;
  text-align: center;
}

.add-layout .add {
  overflow: hidden;
  display: grid;
  grid-template-rows: auto;
  text-align: center;
  justify-content: center;
}
.type{
  padding-top: 30px;
}

/* 头像 */
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}

.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 20px;
  height: 20px;
  text-align: center;
}
</style>