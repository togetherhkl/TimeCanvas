<template>
  <EditI @formSubmit="handleFormSubmit" :fetchData="false" @formReset="handleFormReset" />
</template>
<script>
import EditI from '../components/EditI.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
import { useRouter } from 'vue-router';
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
    };
  },
  components: {
    EditI,
  },
  methods: {
    handleFormSubmit(newData) {
      this.formData = newData;
      const type = this.$router.currentRoute.value.query.type;
      this.formData.event_album_name = type;
      this.formData.event_album_image = type;//趣事录图片，为防止空值，暂时用type代替
      console.log('添加事件里formdata:', this.formData);
      /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
      if (Object.values(this.formData).some(value => !value))
        ElMessageBox.alert('请填写完整信息', '提示', {
          confirmButtonText: '确定',
          type: 'warning'
        });
      else {
        console.log("成功提交");
        axios.post('/interestingevent', this.formData)
          .then(response => {
            // 处理成功响应
            console.log("趣事录创建回应：", response.data);
            this.formData = {};//清空表单,但失败???
            console.log('趣事录创建里formdata:', this.formData);
            ElMessageBox.alert('添加成功', '提示', {
              confirmButtonText: '确定',
              type: 'success'
            }).then(() => {
              // const type = this.$router.currentRoute.value.query.type;
              // this.$router.push({ path: '/趣事录/informshow', query: { stage: type } });
            });
          }).catch(error => {
            // 处理错误响应
            console.log(error);
          });
      }
    },
    handleFormReset() {
      this.formData = {};
    },
  },
}
</script>