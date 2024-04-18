<template>
  <EditC @formSubmit="handleFormSubmit" :fetchData="false" @formReset="handleFormReset"/>
</template>
<script>
import EditC from '../components/EditC.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
export default{
  data(){
    return{
      formData:{
        classmates_album_name:'',
        classmates_avatar_name:'',
        name:'',
        nickname:'',
        birthday:'',
        hometown:'',
        qq_number:'',
        wx_number:'',
        phone_number:'',
        email:'',
        constellation:'',
        hobby:'',
        dream:'',
        graduation_message:'',
      },
    };
  },
  components:{
    EditC,
  },
  methods:{
    handleFormSubmit(newData){
      this.formData=newData;
      const type = this.$router.currentRoute.value.query.type;
      this.formData.classmates_avatar_name = type;
      /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
      if (Object.values(this.formData).some(value => !value))
      ElMessageBox.alert('请填写完整信息', '提示', {
        confirmButtonText: '确定',
        type: 'warning'
      });
      else{
      axios.post('/classmate/', this.formData)
        .then(response => {
          // 处理成功响应
          this.formData={};//清空表单,但失败???
          ElMessageBox.alert('添加成功', '提示', {
            confirmButtonText: '确定',
            type: 'success'
          }).then(() => {
            ElMessageBox.alert('请前往百度网盘上传图片与视频', '提示', {
              confirmButtonText: '确定',
              type: 'info'
            });
            const type = this.$router.currentRoute.value.query.type;
            this.$router.push({ path: '/classmates/informshow',query: { stage: type } });
          });
        })
        .catch(error => {
          // 处理错误响应
          console.error('添加失败:', error);
        });
      }
    },
    handleFormReset(){
      this.formData={};
    },
  },
}
</script>