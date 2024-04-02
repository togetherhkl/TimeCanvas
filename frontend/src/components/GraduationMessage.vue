<template>
    <div class="container">
        <div class="graduation-message">
            <div class="gm-label">
                <i class="iconfont icon-liuyanjiyu"></i>
                <span style="writing-mode: vertical-rl;">毕</span>
                <span style="writing-mode: vertical-rl;">业</span>
                <span style="writing-mode: vertical-rl;">寄</span>
                <span style="writing-mode: vertical-rl;">语</span>
            </div>
            <div class="gm-box">
                {{ graduation_message }}
                <div class="bigdata">
                    <el-button @click="openMessageBox">
                        <i class="iconfont icon-roboticon">AI总结</i>
                    </el-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { ElMessage, ElMessageBox } from 'element-plus';
import type { Action } from 'element-plus';
import axios from 'axios';
import { defineComponent, ref, PropType,watch } from 'vue';

export default defineComponent({
    props: {
    selectedClassmate: {
      type: Object as PropType<any>,
      default: null
    }
  },
  setup(props) {
    const graduation_message = ref('');
    console.log('看:');
    // 从后端API获取毕业寄语数据
   /*  axios.get('/classmate/senior')
      .then(response => {
        const temp =response.data['classmates'];
        const classmateData = temp[0];
        graduation_message.value = classmateData.graduation_message;
      })
      .catch(error => {
        console.error('没有匹配毕业寄语！', error);
      }); */

    // 弹出消息框函数
    const openMessageBox = () => {
      // 在这里添加打开消息框的逻辑
      ElMessageBox.alert('This is a message', 'AI总结', {
        // if you want to disable its autofocus
        //autofocus: false,
        confirmButtonText: 'OK',
    })
    };
    // 监听selectedClassmate变化，更新毕业寄语数据
    watch(() => props.selectedClassmate, (newVal) => {
      if (newVal) {
        graduation_message.value = newVal.graduation_message;
      } else {
        graduation_message.value = '1'; // 清空毕业寄语数据
      }
    });
    return {
      graduation_message,
      openMessageBox
    };
  }
});
const open = () => {
    ElMessageBox.alert('This is a message', ' {{ <i class="iconfont icon-roboticon"></i> }} AI总结', {
        // if you want to disable its autofocus
        // autofocus: false,
        confirmButtonText: 'OK',
    })
}
</script>
<style scoped>
.container {
    margin-top: 1%;
    width: 100%;
}

.graduation-message {
    display: grid;
    grid-template-columns: auto 1fr;
}

.gm-label {
    width: auto;
    height: auto;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
    writing-mode: vertical-rl;
    align-items: center;
    justify-content: center;
}

.gm-box {
    width: 100%;
    padding: 10px;
    align-items: center;
    justify-content: center;
   /*  background-color: antiquewhite; */
    /* position: relative; */
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow:inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.bigdata {
    /* 将按钮居右下 */
    position: absolute;
    bottom: 0;
    right: 0;
    margin-right: 20px;
}
</style>
  