<!-- <template>
    <div>
        <h2>创建趣事录</h2>
        <form @submit.prevent="submitForm">
            <label for="name">趣事录名称:</label>
            <input type="text" id="name" v-model="eventName" required>
            <br>
            <label for="photo">趣事录封面图:</label>
            <input type="file" id="photo" @change="handlePhotoUpload" required>
            <br>
            <button type="submit">提交</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            eventName: '',
            eventphoto: null,
        };
    },
    methods: {
        handlePhotoUpload(event) {
            this.photo = event.target.files[0];
        },
        submitForm() {
            // Perform API call to send eventName and photo to the backend
            // Example using axios:
            const formData = new FormData();
            formData.append('eventName', this.eventName);
            formData.append('photo', this.eventphoto);
            console.log(formData.value);

            axios.post('/api/create-interesting-event', formData)
                .then(response => {
                    // Handle success response
                    console.log(response.data);
                })
                .catch(error => {
                    // Handle error response
                    console.error(error);
                });
        }
    }
};
</script> -->

<template>
  <el-form ref="ruleFormRef" style="max-width: 600px" :model="ruleForm" status-icon :rules="rules" label-width="auto"
    class="demo-ruleForm">
    <el-form-item label="趣事录名称" prop="name">
      <el-input v-model="ruleForm.name" autocomplete="off" />
    </el-form-item>
    <el-form-item label="趣事录封面图" prop="imageUrl">
      <!--  <el-input v-model="ruleForm.imageUrl" autocomplete="off" /> -->
      <el-upload class="upload-demo">
        <img v-if="ruleForm.imageUrl" :src="ruleForm.imageUrl" alt="趣事录封面图" />
        <el-icon v-else class="avatar-uploader-icon">
          <Plus />
        </el-icon>
      </el-upload>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)">提交</el-button>
      <el-button @click="resetForm(ruleFormRef)">取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue';
import type { FormInstance, FormRules } from 'element-plus';
const ruleFormRef = ref<FormInstance>();
const ruleForm = reactive({
  name: '',
  imageUrl: null,
});
const rules = reactive<FormRules<typeof ruleForm>>({
  name: [{ required: true, message: '请输入活动名称', trigger: 'blur' }],
});
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      console.log('submit!');
      console.log(ruleForm);
    } else {
      console.log('error submit!');
      return false
    }
  })
};
const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields();
};
</script>