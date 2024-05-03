<template>
    <el-table :data="filterTableData" style="width: 100%" :stripe="true">
        <el-table-column label="相册类型" prop="album_name" min-width="100">
            <template #default="scope">
                <span v-if="!scope.row.editing">{{ scope.row.album_name }}</span>
                <el-input v-else v-model="scope.row.temp_name" />
            </template>
        </el-table-column>
        <el-table-column label="相册描述" prop="album_description">
            <template #default="scope">
                <span v-if="!scope.row.editing">{{ scope.row.album_description }}</span>
                <el-input v-else v-model="scope.row.temp_description" />
            </template>
        </el-table-column>
        <el-table-column label="相关操作" align="right">
            <template #default="scope">
                <el-button type="info" @click="handleEdit(scope.row)"><el-icon>
                        <Edit />
                    </el-icon>编辑</el-button>
                <el-button type="primary" @click="handleSave(scope.row)"><el-icon><Select /></el-icon>保存</el-button>
                <el-button type="danger" @click="handleDelete(scope.row)"><el-icon>
                        <Delete />
                    </el-icon>删除</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>

<script lang="ts">
import { ref, onMounted, defineComponent } from 'vue';
import axios from 'axios';
import { ElMessage,ElLoading} from 'element-plus';

interface filterTableData {
    id: number;
    album_type: number;
    album_name: string;
    album_description: string;
    editing: boolean;
    originalData: {
        album_name: string;
        album_description: string;
    };
    temp_name: string;
    temp_description: string;
}

export default defineComponent({
    setup() {
        const filterTableData = ref<filterTableData[]>([]);
        const fetchChartData = async () => {
            try {
                const loadingInstance = ElLoading.service({ fullscreen: true });
                const res = await axios.get('/albumtype');
                let ids = await res.data.map((item: { id: any; }) => item.id);
                for (let id of ids) {
                    const response = await axios('/album', { params: { album_type_id: id } });
                    const data = await response.data;
                    filterTableData.value = filterTableData.value.concat(data.map((item: filterTableData) => ({
                        ...item,
                        editing: false
                    })));
                }loadingInstance.close();
            } catch (error) {
                console.error('Error:', error);
            }
        };

        onMounted(() => {
            fetchChartData();
        });

        const handleEdit = (row: filterTableData) => {
            if (!row.editing) {
                row.originalData = { ...row };
                row.temp_name = row.album_name; //保存相册名的临时值
                row.temp_description = row.album_description; // 保存相册描述的临时值
            } else {//取消编辑
                row.album_name = row.originalData.album_name;
                row.album_description = row.originalData.album_description;
            }
            row.editing = !row.editing;
        };

        const handleSave = async (row: filterTableData) => {
            try {
                const res = await axios.put('/album', {
                    album_name: row.temp_name,
                    album_description: row.temp_description
                }, { params: { id: row.id } });
                ElMessage.success('保存成功');
                row.editing = false; //编辑状态变为false
                row.album_name = row.temp_name; // 保存相册名
                row.album_description = row.temp_description; // 保存相册描述
            } catch (error) {
                ElMessage.error('保存失败');
                row.album_name = row.originalData.album_name;
                row.album_description = row.originalData.album_description;
            }
        };

        const handleDelete = async (row: filterTableData) => {
            try {
                /* 先通过album_type数字去取对应的get,并且将album_name传参获得所有事件的id，通过获得的id依次删除数据，最后再删除album里的数据 */
                const tempid = row.album_type;
                if (tempid == 1) {
                    await axios.get(`/classmate/${row.album_name}`).then((res) => {
                        // console.log('同学：',res.data);
                        for (let i = 0; i < res.data.classmates.length; i++) {
                            axios.delete('/classmate/', { params: { id: res.data.classmates[i].id } }).then((res) => {
                                if (res.status === 200) {
                                    let path = "/apps/TimeGallery/同学录/" + row.album_name;
                                    let filepath = [''];path = path.replace(/'/g, '"');//把单引号替换成双引号
                                    filepath.push(path)
                                    axios.delete("/baidufile/deletefile", { data: filepath }).then((res) => {
                                        if (res.data.erron == 2) {
                                            ElMessage.error(`删除${row.album_name}相册内的图库失败！`);
                                        } else { ElMessage.success(`删除${row.album_name}相册成功！`); }
                                    });
                                } else { ElMessage.error(`删除${row.album_name}失败`); }
                            });
                        }
                    });
                } else if (tempid == 2) {
                    await axios.get('/interestingevent', { params: { event_album_name: row.album_name } }).then((res) => {
                        console.log('事件：', res.data);
                        for (let i = 0; i < res.data.length; i++) {
                            // console.log('列表：',res.data[i].id)
                            axios.delete('/interestingevent', { params: { id: res.data.interesting_events[i].id } }).then((res) => {
                                if (res.status === 200) {
                                    let path = "/apps/TimeGallery/趣事录/" + row.album_name;
                                    let filepath = [''];path = path.replace(/'/g, '"');//把单引号替换成双引号
                                    filepath.push(path)
                                    axios.delete("/baidufile/deletefile", { data: filepath }).then((res) => {
                                        if (res.data.erron == 2) {
                                            ElMessage.error(`删除${row.album_name}相册内的图库失败！`);
                                        } else { ElMessage.success(`删除${row.album_name}相册成功！`); }
                                    });
                                } else { ElMessage.error(`删除${row.album_name}失败`); }
                            });
                        }
                    });
                } else {
                    await axios.get('/travel', { params: { travel_album_name: row.album_name } }).then((res) => {
                        // console.log('旅游：',res.data);
                        for (let i = 0; i < res.data.length; i++) {
                            axios.delete('/travel', { params: { id: res.data[i].id } }).then((res) => {
                                if (res.status === 200) {
                                    let path = "/apps/TimeGallery/旅游志/" + row.album_name;
                                    let filepath = [''];path = path.replace(/'/g, '"');//把单引号替换成双引号
                                    filepath.push(path)
                                    axios.delete("/baidufile/deletefile", { data: filepath }).then((res) => {
                                        if (res.data.erron == 2) {
                                            ElMessage.error(`删除${row.album_name}相册内的图库失败！`);
                                        } else { ElMessage.success(`删除${row.album_name}相册成功！`); }
                                    });
                                } else { ElMessage.error(`删除${row.album_name}失败`); }
                            });
                        }
                    });
                }
                await axios.delete('/album', { params: { album_id: row.id } });
                filterTableData.value = filterTableData.value.filter(item => item.id !== row.id);// Delete the row from the table
                ElMessage.success('删除成功');
            } catch (error) {
                console.error('删除失败:', error);
            }
        };

        return {
            filterTableData,
            handleEdit,
            handleSave,
            handleDelete,
        };
    }
});
</script>
