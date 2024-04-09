<template>
    <EditC @formSubmit="handleFormSubmit" :fetchData="true" @formReset="handleFormReset" />
</template>

<script>
import EditC from '../components/EditC.vue';
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
        EditC,
    },
    methods: {
        handleFormSubmit(newData) {
            this.formData=newData;
            console.log('formdata:',this.formData);
            const id = this.$router.currentRoute.value.query.id;
            console.log('id:',id);
            /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
            if (Object.values(this.formData).some(value => !value)) 
            ElMessageBox.alert('请填写完整信息', '提示', {
                confirmButtonText: '确定',
                type: 'warning'
            });
            else{
            axios.put('/classmate/', this.formData, { params: { id:id } })
                .then(response => {
                    console.log(response.data);
                    // this.formData={};//清空表单,但失败???
                    ElMessageBox.alert('修改成功', '提示', {
                        confirmButtonText: '确定',
                        type: 'success'
                    }).then(() => {
                        // const type = this.$router.currentRoute.value.query.type;
                        // this.$router.push({ path: '/classmates/informshow',query: { stage: type } });
                    })
                })
                .catch(error => {
                    console.error(error);
                });
            }
        },
        handleFormReset() {
            console.log('reset');
            this.formData={};
        },
    },
};
</script>