<template>
  <EditT @formSubmit="handleFormSubmit" :fetchData="false"/>
</template>
<script>
import EditT from '../components/EditT.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
import { useRouter } from 'vue-router';
export default {
  data() {
    return {
      formData: {
        travel_theme: '',//旅游主题
        travel_date: '',//旅游日期
        travel_description: '',//旅游描述
        travel_participant: '',//旅游参与者
        travel_place: '',//旅游具体地点
        travel_province:'',//旅游省份
        travel_album_name:'',
      },
    };
  },
  components: {
    EditT,
  },
  methods: {
    handleFormSubmit(newData) {
      this.formData = newData;
      const type = this.$router.currentRoute.value.query.type;
      this.formData.travel_album_name=type;
      /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
      if (Object.values(this.formData).some(value => !value))
        ElMessageBox.alert('请填写完整信息', '提示', {
          confirmButtonText: '确定',
          type: 'warning'
        });
      else {
        console.log("成功提交");
        axios.post('/travel',this.formData)
        .then(() => {
            ElMessageBox.alert('添加成功', '提示', {
              confirmButtonText: '确定',
              type: 'success'
            }).then(() => {
              const type = this.$router.currentRoute.value.query.type;
              this.$router.push({ path: '/travels/informshow', query: { stage: type } });
            });
          }).catch(error => {
            // 处理错误响应
            console.log(error);
          });
      }
    },
  },
}
</script>