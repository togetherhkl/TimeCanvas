<template>
    <EditI @formSubmit="handleFormSubmit" :fetchData="true" />
</template>
I
<script>
import EditI from '../components/EditI.vue';
import axios from 'axios';
import { ElMessageBox, ElLoading } from 'element-plus';
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
            const id = this.$router.currentRoute.value.query.id;
            /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
            if (Object.values(this.formData).some(value => !value))
                ElMessageBox.alert('请填写完整信息', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
            else {
                const loading = ElLoading.service({ fullscreen: true });
                axios.put('/interestingevent/', this.formData, { params: { id: id } }).then(() => {
                    loading.close();
                    ElMessageBox.alert('修改成功', '提示', {
                        confirmButtonText: '确定',
                        type: 'success'
                    }).then(() => {
                        this.$router.push({ path: '/interestingevents/informshow', query: { stage: type } });
                    })
                }).catch(error => { loading.close(); console.error(error); });
            }
        },
    },
};
</script>