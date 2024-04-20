<template>
    <div class="gmlayout">
        <div class="title1">文本输入</div>
        <div class="title2">AI辅助创作</div>
        <div>
            <div id="vditor"></div>
        </div>
        <div class="backai">
            <textarea id="aiinput" style="height: 200px;" v-model="aiinput" placeholder="请输入AI辅助创作的要求"></textarea>
            <el-button class="aibutton" @click="getAI">AI</el-button>
            <div class="ailoading" style="width: 100%;" >
            <textarea v-loading="loading" style="height: 215px;"
                placeholder="AI辅助创作的结果">{{ aioutput }}</textarea>
            </div>
        </div>
    </div>
</template>
<script>
import { onMounted, ref, watch } from 'vue';
import axios from 'axios';
import Vditor from 'vditor';
import 'vditor/dist/index.css';
import { ElLoading } from 'element-plus';
export default {
    setup(props, { emit }) {
        const aiinput = ref('');//AI分析的要求
        const aioutput = ref('');//AI生成的文本
        const loading = ref(false);//加载状态
        const vditor = ref(null);//编辑器
        const vditortext = ref('');//编辑器内容

        onMounted(() => {
            const vditor = new Vditor('vditor', {
                height: 500,
                toolbarConfig: {
                    pin: true,
                },
                cache: {
                    enable: false,
                },
                mode: 'wysiwyg',
                preview: {
                    theme: {
                        current: 'dark',
                    },
                    mode: 'both',
                },
                typewriterMode: true,
                theme: 'dark',
                input(value) {
                    vditortext.value = value;//编辑器内容
                    emit('update-vditortext', vditortext.value);
                },
            });
        });
        return {
            vditor,
            loading,
            aiinput,
            aioutput,
            loading
        };
    },
    methods: {
        getVditor() {
            console.log(this.vditor);
        },
        //获取后端ai返回的数据
        async getAI() {
            console.log("加载动画")
            const loadai = ElLoading.service({
                lock: true,
                text: 'Loading',
                background: 'rgba(0, 0, 0, 0.7)',
                target: document.querySelector('.ailoading'),
            })
            axios.get('/xunfei/semantic/textcreat', {
                params: {
                    text: JSON.stringify(this.aiinput),
                }
            }).then(response => {
                // 处理成功响应
                if (response.status == 200) {
                    this.aioutput = response.data;
                    loadai.close()//添加动画没有效果
                } else {
                    console.log('AI生成失败!');
                }
            }).catch(error => {
                // 处理错误响应
                console.error('哦豁，后端问题:', error);
            });
        },
    },
};
</script>
<style scoped>
#vditor {
    width: 100%;
    height: 100%;
}

.gmlayout {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 10px;
}

.title1,
.title2 {
    margin: 0;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #000;
}

.backai {
    display: grid;
    grid-template-rows: 1fr auto 1fr;
}

.backai>* {
    margin-bottom: 10px;
}

.backai textarea {
    width: 100%;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.aibutton {
    width: 100px;
    background-color: #c88dee;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
    transition: all 0.3s;
}

.aibutton:active {
    background-color: #b3a5fa;
}

.aibutton:hover {
    background-color: #b3a5fa;
}
</style>