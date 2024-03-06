<template>
    <div class="add-layout">
      <div class="add-title">
        <h1>添加有趣事件信息</h1>
      </div>
      <div class="add">
        <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="150px" class="demo-ruleForm"
          :size="formSize" status-icon>
          <div class="eventname">
            <el-form-item label="事件名称" prop="eventname">
              <el-radio-group v-model="ruleForm.eventname">
                <el-radio label="篮球" />
                <el-radio label="足球" />
                <el-radio label="羽毛球" />
                <el-radio label="拔河" />
              </el-radio-group>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="事件日期" prop="eventdate">
                <el-date-picker v-model="ruleForm.eventdate" type="date" label="Pick a date" style="width: 100%" />
            </el-form-item>
          </div>
          <div>
            <el-form-item label="事件参与者" prop="eventparticipant">
                <el-input v-model="ruleForm.eventparticipant" />
            </el-form-item>
          </div>
          <div>
            <el-form-item label="事件描述" prop="eventdescription">
                <el-input v-model="ruleForm.eventdescription" />
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
  import { reactive, ref } from 'vue'
  import type { FormInstance, FormRules } from 'element-plus'
  import { ElForm, ElFormItem, ElCheckboxGroup, ElCheckbox, ElInput, ElButton } from 'element-plus';
  
  const form = ref({
    hobby: [] as string[]
  });
  const newHobby = ref('');
  
  const addnewHobby = () => {
    if (newHobby.value) {
      form.value.hobby.push(newHobby.value);
      newHobby.value = '';
    }
    console.log(ruleForm.eventname);
  };
  
  interface RuleForm {
    eventname:string,
    eventdate:string,
    eventdescription:string,
    eventparticipant:string,
  }
  
  const formSize = ref('default')
  const ruleFormRef = ref<FormInstance>()
  const ruleForm = reactive<RuleForm>({
    eventname:'',
    eventdate:'',
    eventdescription:'',
    eventparticipant:'',
  })
  //规则
  const rules = reactive<FormRules<RuleForm>>({
    eventname: [
      { required: true, message: '请选择添加的同学录相册名称', trigger: 'blur' }
    ],
    eventdate: [
      {
        type: 'date',
        required: true,
        message: '请输入生日',
        trigger: 'change',
      },
    ],
    eventdescription: [
      { required: true, message: '请输入事件描述', trigger: 'blur' },
    ],
  })
  //提交表单
  const submitForm = async (formEl: FormInstance | undefined) => {
    if (!formEl) return
    await formEl.validate((valid, fields) => {
      if (valid) {
        console.log('submit!');
        console.log(ruleForm);
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