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
                毕业寄语
                <div class="bigdata">
                    <el-button @click="open">AI总结</el-button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script lang="ts" setup>
import { ElMessage, ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'

const open = () => {
    ElMessageBox.alert('This is a message', '关键词展示', {
        // if you want to disable its autofocus
        // autofocus: false,
        confirmButtonText: 'OK',
    })
}
</script>
<style scoped>
.container {
    margin-top: 1%;
    display: flex;
}

.graduation-message {
    display: grid;
    grid-template-columns: 1fr 17fr;
}

.gm-label {
    height: auto;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
    writing-mode: vertical-rl;
}

.gm-box {
    padding: 10px;
    align-items: center;
    justify-content: center;
   /*  background-color: antiquewhite; */
    position: relative;
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
}</style>
  