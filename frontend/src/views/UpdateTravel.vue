<template>
    <EditT @formSubmit="handleFormSubmit" :fetchData="true" @formReset="handleFormReset" />
</template>

<script>
import EditT from '../components/EditT.vue';
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
        EditT,
    },
    methods: {
        handleFormSubmit(newData) {
            this.formData = newData;
            const type = this.$router.currentRoute.value.query.type;
            this.formData.travel_album_name = type;
            console.log('更新旅游志里formdata:', this.formData);
            const id = this.$router.currentRoute.value.query.id;
            console.log('id:', id);
            /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
            if (Object.values(this.formData).some(value => !value))
                ElMessageBox.alert('请填写完整信息', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
            else {
                axios.put('/travel/', this.formData, { params: { id: id } })
                    .then(response => {
                        // 处理成功响应
                        console.log(response.data);
                        this.formData = {};//清空表单,但失败???
                        ElMessageBox.alert('修改成功', '提示', {
                            confirmButtonText: '确定',
                            type: 'success'
                        }).then(() => {
                            const type = this.$router.currentRoute.value.query.type;
                            this.$router.push({ path: '/travels/informshow', query: { stage: type } });
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