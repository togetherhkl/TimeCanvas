<template>
  <EditT @formSubmit="handleFormSubmit" :fetchData="false" @formReset="handleFormReset" />
</template>
<script>
import EditT from '../components/EditT.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
export default {
  data() {
    return {
      formData: {
        travel_theme: '',//旅游主题
                travel_date: '',//旅游日期
                travel_description: '',//旅游描述
                travel_participant: '',//旅游参与者
                travel_place: '',//旅游地点
      },
    };
  },
  components: {
    EditT,
  },
  methods: {
    handleFormSubmit(newData) {
      this.formData = newData;
      console.log('添加旅游里formdata:', this.formData);
      /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
      if (Object.values(this.formData).some(value => !value))
        ElMessageBox.alert('请填写完整信息', '提示', {
          confirmButtonText: '确定',
          type: 'warning'
        });
      else {
        console.log("成功提交");
      }
    },
    handleFormReset() {
      this.formData = {};
    },
  },
}
</script>