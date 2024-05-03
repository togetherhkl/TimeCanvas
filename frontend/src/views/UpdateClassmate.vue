<template>
    <EditC @formSubmit="handleFormSubmit" :fetchData="true" />
</template>

<script>
import EditC from '../components/EditC.vue';
import axios from 'axios';
import { ElMessageBox, ElLoading } from 'element-plus';
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
            this.formData = newData; const type = this.$router.currentRoute.value.query.type;
            const id = this.$router.currentRoute.value.query.id;
            /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
            if (Object.values(this.formData).some(value => !value))
                ElMessageBox.alert('请填写完整信息', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
            else {
                const loadingInstance = ElLoading.service({ fullscreen: true });
                axios.put('/classmate/', this.formData, { params: { id: id } }).then(() => {
                    loadingInstance.close();
                    ElMessageBox.alert('修改成功', '提示', {
                        confirmButtonText: '确定', type: 'success'
                    }).then(() => {
                        this.$router.push({ path: '/classmates/informshow', query: { stage: type } });
                    });
                });
            }
        },
        handleFormReset() {
            console.log("reset");
            this.formData = {};
        },
    },
};
</script>