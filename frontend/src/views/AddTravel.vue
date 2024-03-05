<template>
    <div class="add-layout">
      <div class="add-title">
        <h1>添加旅游信息</h1>
      </div>
      <div class="add">
        <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="150px" class="demo-ruleForm"
          :size="formSize" status-icon>
          <div class="travelalbumtname">
            <el-form-item label="旅游相册名称" prop="travelalbumname">
              <el-radio-group v-model="ruleForm.travelalbumname">
                <el-radio label="旅游1号" />
                <el-radio label="旅游2号" />
                <el-radio label="旅游3号" />
                <el-radio label="旅游4号" />
              </el-radio-group>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="旅游主题" prop="traveltheme">
                <el-input v-model="ruleForm.traveltheme" />
            </el-form-item>
          </div>
          <div>
            <el-form-item label="旅游日期" prop="traveldate">
                <el-date-picker v-model="ruleForm.traveldate" type="date" label="Pick a date" style="width: 100%" />
            </el-form-item>
          </div>
          <div>
            <el-form-item label="旅游参与者" prop="travelparticipant">
                <el-input v-model="ruleForm.travelparticipant" />
            </el-form-item>
          </div>
          <div>
            <el-form-item label="旅游地点" prop="travelplace">
                <el-input v-model="ruleForm.travelplace" />
            </el-form-item>
          </div>
          <div>
            <el-form-item label="旅游描述" prop="traveldescription">
                <el-input v-model="ruleForm.traveldescription" />
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
  interface RuleForm {
    travelalbumname:string,
    traveltheme:string,
    traveldate:string,
    travelparticipant:string,
    travelplace:string,
    traveldescription:string,
  }
  
  const formSize = ref('default')
  const ruleFormRef = ref<FormInstance>()
  const ruleForm = reactive<RuleForm>({
    travelalbumname:'',
    traveltheme:'',
    traveldate:'',
    travelparticipant:'',
    travelplace:'',
    traveldescription:'',
  })
  //规则
  const rules = reactive<FormRules<RuleForm>>({
    travelalbumname: [
      { required: true, message: '请选择添加的同学录相册名称', trigger: 'blur' }
    ],
    traveldate: [
      {
        type: 'date',
        required: true,
        message: '请输入旅游日期',
        trigger: 'change',
      },
    ],
    traveldescription: [
      { required: true, message: '请输入旅游描述', trigger: 'blur' },
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