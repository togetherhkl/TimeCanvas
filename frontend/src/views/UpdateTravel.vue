<template>
    <EditT @formSubmit="handleFormSubmit" :fetchData="true" />
</template>

<script>
import EditT from '../components/EditT.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
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
            this.formData.travel_album_image = type;//旅游图片，为防止空值，暂时用type代替
            const id = this.$router.currentRoute.value.query.id;
            /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
            if (Object.values(this.formData).some(value => !value))
                ElMessageBox.alert('请填写完整信息', '提示', {
                    confirmButtonText: '确定',
                    type: 'warning'
                });
            else {
                axios.put('/travel/', this.formData, { params: { id: id } })
                    .then(() => {
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
    },
};
</script>