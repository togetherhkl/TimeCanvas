<template>
    <EditI @formSubmit="handleFormSubmit" :fetchData="true" @formReset="handleFormReset" />
</template>
I
<script>
import EditI from '../components/EditI.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
import { useRoute } from 'vue-router';
export default {
    data() {
        return {
            formData: {},
        };
    },
    components: {
        EditI,
    },
    methods: {
        handleFormSubmit(newData) {
            // 在这里将表单数据传到后端
            this.formData = newData;
            const type = this.$router.currentRoute.value.query.type;
            this.formData.event_album_name = type;
            this.formData.event_album_image = type;//趣事录图片，为防止空值，暂时用type代替
            console.log('趣事录更新里formdata:', this.formData);
            const id = this.$router.currentRoute.value.query.id;
            console.log('id:', id);
            /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
            if (Object.values(this.formData).some(value => !value))
                ElMessageBox.alert('请填写完整信息', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
            else {
                axios.put('/interestingevent/', this.formData, { params: { id: id } })
                    .then(response => {
                        // 处理成功响应
                        console.log(response.data);
                        this.formData = {};//清空表单,但失败???
                        ElMessageBox.alert('修改成功', '提示', {
                            confirmButtonText: '确定',
                            type: 'success'
                        }).then(() => {
                            const type = this.$router.currentRoute.value.query.type;
                            this.$router.push({ path: '/interestingevents/informshow',query: { stage: type } });
                        })
                    })
                    .catch(error => {
                        // 处理错误响应
                        console.error(error);
                    });
            }
        },
        handleFormReset() {
            console.log('reset');
            this.formData = {};
        },
    },
};
</script>