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
        <div class="gm-text" v-html="markdownToHtml"></div>
        <div class="bigdata">
          <el-button @click="openMessageBox">
            <i class="iconfont icon-roboticon">AI总结</i>
          </el-button>
        </div>
      </div>
    </div>
  </div>
  <el-dialog overflow :close-on-click-modal="false" :modal="false" v-model="dialogOverflowVisible"
    title="AI文字提炼与总结" width="600" draggable>
    <div v-loading="loading" class="aishow">
      <div v-html="aireutohtml"></div>
    </div>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogOverflowVisible = false">关闭</el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts">
import { ElMessage, ElMessageBox } from 'element-plus';
import axios from 'axios';
import { defineComponent, ref, PropType, watch } from 'vue';
import { marked, options } from 'marked';//markdown解析器
import { set } from 'video.js/dist/types/tech/middleware';
export default defineComponent({
  props: {
    selectedClassmate: {
      type: Object as PropType<any>,
      default: null
    }
  },
  computed: {
    markdownToHtml() {
      return marked(this.graduation_message);
    },
    aireutohtml() {
      return marked(this.airesult);
    }
  },
  setup(props) {
    const graduation_message = ref('');
    const airesult = ref('');
    const dialogOverflowVisible = ref(false)
    const loading = ref(false);
    // 弹出消息框函数
    const openMessageBox = () => {
      // 在这里添加打开消息框的逻辑
      dialogOverflowVisible.value = true;
      loading.value = true;
      axios.get('/xunfei/semantic/textanl', {
        params: {
          text: JSON.stringify(graduation_message.value),
        }
      }).then(
        response => {
          if (response.status == 200) {
            airesult.value  = response.data;
            loading.value = false;
          }else {
            ElMessage.error('AI总结失败！');
          }
        }
      )
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
      airesult,
      dialogOverflowVisible,
      loading,
      openMessageBox
    };
  }
});
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
  background: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.gm-text {
  width: 100%;
  min-height: 100px;
  height: auto;
  font-size: 16px;
}

.bigdata {
  /* 将按钮居右下 */
  position: absolute;
  bottom: 0;
  right: 0;
  margin-right: 20px;
}

.aishow {
  widows: 300px;
  height: 300px;
  overflow: auto;
  font-size: 18px; /* 调整字体大小 */
  color: #333; /* 调整字体颜色 */
  font-family: 'Arial', sans-serif; /* 调整字体家族 */
  line-height: 1.5; /* 调整行高 */
  text-align: justify; /* 对齐文本 */
}
</style>