<template>
  <EditI @formSubmit="handleFormSubmit" :fetchData="false" @formReset="handleFormReset" />
</template>
<script>
import EditI from '../components/EditI.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
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
      console.log('添加事件里formdata:', this.formData);
      /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
      if (Object.values(this.formData).some(value => !value))
        ElMessageBox.alert('请填写完整信息', '提示', {
          confirmButtonText: '确定',
          type: 'warning'
        });
      else {
        console.log("成功提交");
        const type = this.$router.currentRoute.value.query.type;
        this.$router.push({path:'/趣事录/informshow',query:{stage:type}});
      }
    },
    handleFormReset() {
      this.formData = {};
    },
  },
}
</script>