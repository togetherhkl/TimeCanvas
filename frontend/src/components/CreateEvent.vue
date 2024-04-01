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
  <div class="title">创建{{ title }}</div>
  <el-form ref="ruleFormRef" style="max-width: 600px" :model="ruleForm" status-icon :rules="rules" label-width="auto"
    class="demo-ruleForm">
    <el-form-item :label="title+'名称'" prop="album_name">
      <el-input v-model="ruleForm.album_name" autocomplete="off" />
    </el-form-item>
    <el-form-item :label="title+'描述'" prop="album_description">
      <el-input type="textarea" v-model="ruleForm.album_description" autocomplete="off" />
    </el-form-item>
    <el-form-item :label="title+'封面图'" prop="album_cover">
       <!-- <el-input v-model="ruleForm.album_cover" autocomplete="off" /> -->
      <el-upload class="upload-demo" :show-file-list="false" :before-upload="beforeUpload" :on-success="handleUploadSuccess">
        <img v-if="ruleForm.album_cover" :src="ruleForm.album_cover" style="max-width: 200px;max-height: 200px;" alt="趣事录封面图" />
        <el-icon v-else class="avatar-uploader-icon">
          <Plus />
        </el-icon>
      </el-upload>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm()">提交</el-button>
      <el-button @click="resetForm()">取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';
export default{
  props:['title'],
  data(){
    return{
      ruleForm:{
        album_name:'',
        // album_cover:'',
        album_description:'',//趣事录描述
        album_type:0,
      },
      rules:{
        album_name:[
          {required:true,message:`请输入${ this.title }名称`,trigger:'blur'}
        ],
        album_description:[
          {required:true,message:`请描述${ this.title }`,trigger:'blur'}
        ],
        // album_cover:[
        //   {required:true,message:`请上传${ this.title }封面图`,trigger:'blur'}
        // ],
      }
    }
  },
  methods:{
    beforeUpload(file){
      console.log('file',file);
      console.log('开始');
      const url=URL.createObjectURL(file);//将文件转为url
      this.ruleForm.album_cover=url;
      console.log('url',this.ruleForm.album_cover);
      return false;//阻止默认上传
    },
    handleUploadSuccess(response,file){
      if(response.code === 200){
        this.ruleForm.album_cover = response.data.url;
        console.log('上传成功',response.data.url);
      }else{
        this.$message.error('上传失败');
      }  
    },
    submitForm(){
      this.$refs.ruleFormRef.validate((valid)=>{
        if(valid){
          console.log('提交成功!');
          if(this.title === '趣事录'){
            this.ruleForm.album_type = 2;
          }else if(this.title === '旅游志'){
            this.ruleForm.album_type = 3;
          }
          console.log(this.ruleForm);
          //发送请求
          axios.post('/album',this.ruleForm).then(response=>{
            console.log(response.data);
          }).catch(error=>{
            console.log(error);
          });
        }else{
          console.log('提交错误!!');
          return false;
        }
      });
    },
    resetForm(){
      this.$refs.ruleFormRef.resetFields();
    },
  }
}
</script>
<style scoped>
.title{
  font-size: 20px;
  margin-bottom: 20px;
  text-align: center;
}
.upload-demo{
  display: inline-block;
}
.avatar-uploader-icon{
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