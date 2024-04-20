<template>
  <div class="title">创建{{ title }}</div>
  <el-form ref="ruleFormRef" style="max-width: 600px" :model="ruleForm" status-icon :rules="rules" label-width="auto"
    class="demo-ruleForm">
    <el-form-item :label="title + '名称'" prop="album_name">
      <el-input v-model="ruleForm.album_name" autocomplete="off" />
    </el-form-item>
    <el-form-item :label="title + '描述'" prop="album_description">
      <el-input type="textarea" v-model="ruleForm.album_description" autocomplete="off" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm()">提交</el-button>
      <el-button @click="resetForm()">取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';
export default {
  props: ['title'],
  data() {
    return {
      ruleForm: {
        album_name: '',
        // album_cover:'',
        album_description: '',//趣事录描述
        album_type: 0,
      },
      rules: {
        album_name: [{ required: true, message: `请输入${this.title}名称`, trigger: 'blur' }],
        album_description: [{ required: true, message: `请描述${this.title}`, trigger: 'blur' }],
      }
    }
  },
  methods: {
    submitForm() {
      this.$refs.ruleFormRef.validate((valid) => {
        if (valid) {
          if (this.title === '同学录') {
            this.ruleForm.album_type = 1;
          }
          else if (this.title === '趣事录') {
            this.ruleForm.album_type = 2;
          } else if (this.title === '旅游志') {
            this.ruleForm.album_type = 3;
          }
          //发送请求
          axios.post('/album', this.ruleForm).then(response => {
            if (response.status == 200) {
              ElMessage.success('提交成功!');
              ElMessageBox.alert('相册封面图请到百度网盘的相应目录下添加', '提示', {
                confirmButtonText: '确定',
                type: 'info',
              }).then(() => {
                this.$router.go(0);
              });
            } else {
              ElMessage.error('提交失败');
            }
          }).catch(error => {
            console.log(error);
          });
        } else {
          ElMessage.error('请检查输入是否正确');
          return false;
        }
      });
    },
    resetForm() {
      this.$refs.ruleFormRef.resetFields();
    },
  }
}
</script>
<style scoped>
.title {
  font-size: 20px;
  margin-bottom: 20px;
  text-align: center;
}

.upload-demo {
  display: inline-block;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 200px;
  height: 200px;
  line-height: 200px;
  text-align: center;
  border: 1px dashed #d9d9d9;
  border-radius: 4px;
}
</style>