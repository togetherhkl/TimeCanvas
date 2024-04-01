<template>
  <div class="add-classmates">
    <div class="add-card">
      <div class="title">{{ type }}时光卡片</div>
      <!-- <el-form :label-position="right" @submit.prevent="submitForm"> -->
      <el-form :label-position="right" :model="formData">
        <div class="layout">
          <div>
            <el-form-item label="姓名" prop="name">
              <el-input class="input" v-model="formData.name" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="昵称" prop="nickname">
              <el-input v-model="formData.nickname" required></el-input>
            </el-form-item>
          </div>
          <div class="avatar">
            <el-form-item label="头像" prop="classmates_avatar_name">
              <el-input v-model="formData.classmates_avatar_name" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="生日" prop="birthday">
              <el-input type="date" v-model="formData.birthday" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="家乡" prop="hometown">
              <el-input v-model="formData.hometown" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="QQ" prop="qq_number">
              <el-input v-model="formData.qq_number" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="微信" prop="wx_number">
              <el-input v-model="formData.wx_number" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="手机号" prop="phone_number">
              <el-input v-model="formData.phone_number" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="formData.email" required></el-input>
            </el-form-item>
          </div>
          <div>
            <el-form-item label="星座" prop="constellation">
              <el-select v-model="formData.constellation" placeholder="请选择" required>
                <el-option label="白羊座" value="白羊座">
                  <i class="iconfont icon-muyangzuo">白羊座</i>
                </el-option>
                <el-option label="金牛座" value="金牛座">
                  <i class="iconfont icon-jinniuzuo">金牛座</i>
                </el-option>
                <el-option label="双子座" value="双子座">
                  <i class="iconfont icon-shuangzizuo">双子座</i>
                </el-option>
                <el-option label="巨蟹座" value="巨蟹座">
                  <i class="iconfont icon-juxiezuo">巨蟹座</i>
                </el-option>
                <el-option label="狮子座" value="狮子座">
                  <i class="iconfont icon-shizizuo">狮子座</i>
                </el-option>
                <el-option label="处女座" value="处女座">
                  <i class="iconfont icon-chunvzuo">处女座</i>
                </el-option>
                <el-option label="天秤座" value="天秤座">
                  <i class="iconfont icon-tianchengzuo">天秤座</i>
                </el-option>
                <el-option label="天蝎座" value="天蝎座">
                  <i class="iconfont icon-tianhezuo">天蝎座</i>
                </el-option>
                <el-option label="射手座" value="射手座">
                  <i class="iconfont icon-sheshouzuo">射手座</i>
                </el-option>
                <el-option label="摩羯座" value="摩羯座">
                  <i class="iconfont icon-mojiezuo">摩羯座</i>
                </el-option>
                <el-option label="水瓶座" value="水瓶座">
                  <i class="iconfont icon-shuipingzuo">水瓶座</i>
                </el-option>
                <el-option label="双鱼座" value="双鱼座">
                  <i class="iconfont icon-shuangyuzuo">双鱼座</i>
                </el-option>
              </el-select>
            </el-form-item>
          </div>
        </div>
        <div class="off">
          <div class="hobby">
            <el-form-item label="爱好" prop="hobby">
              <el-input v-model="formData.hobby" required type="textarea"></el-input>
            </el-form-item>
          </div>
          <div class="mengxiang">
            <el-form-item label="梦想" prop="dream">
              <el-input v-model="formData.dream" required type="textarea"></el-input>
            </el-form-item>
          </div>
          <div class="biyejiyu">
            <el-form-item label="毕业寄语" prop="graduation_message">
              <el-input v-model="formData.graduation_message" required type="textarea"></el-input>
              <button @click="getai">AI</button>
              <div id="editor"></div>
              <!-- <button>AI</button> -->
              <!-- <div id="graduation-message-editor"></div> -->
            </el-form-item>
          </div>
        </div>
        <div class="button">
          <el-button type="submit" @click="submitForm">确认</el-button>
          <el-button type="button" @click="resetForm">重置</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import EditorJS from '@editorjs/editorjs';//引入编辑器
import paragraph from '@editorjs/paragraph';//引入编辑器段落模块
import axios from 'axios';//引入axios
export default {
  data() {
    return {
      formData: {
        classmates_album_name: '',
        classmates_avatar_name: '',
        name: '',
        nickname: '',
        birthday: '',
        hometown: '',
        qq_number: '',
        wx_number: '',
        phone_number: '',
        email: '',
        constellation: '',
        hobby: '',
        dream: '',
        graduation_message: '',
      },
      avatarPreview: '',//头像预览
      type: '',//时光回溯类型
      ediotr: null,//编辑器
    };
  },
  watch: {
    '$route.query.type': {
      immediate: true,
      handler(newVal) {
        this.type = newVal;
        console.log('type', this.type);
      },
    },
  },
  methods: {
    // 处理头像上传
    handleAvatarChange(event) {
      this.formData.classmates_avatar_name = event.target.files[0];
      this.avatarPreview = URL.createObjectURL(event.target.files[0]);
    },
    // 提交表单
    submitForm() {
      console.log(this.formData);
      this.formData.classmates_album_name = this.type;
      console.log(this.formData.classmates_avatar_name);
      console.log('改后', this.formData);
      /* 如果表单为空，则返回；不为空，则将数据发送给数据库 */
      // if (!this.formData) return;
      // axios.post('/classmate/', this.formData)
      //   .then(response => {
      //     // 处理成功响应
      //     console.log(response.data);
      //   })
      //   .catch(error => {
      //     // 处理错误响应
      //     console.error(error);
      //   });
      //   this.resetForm();
    },
    resetForm() {
      // 重置表单数据
      this.formData = {
        classmates_album_name: '',
        classmates_avatar_name: '',
        name: '',
        nickname: '',
        birthday: '',
        hometown: '',
        qq_number: '',
        wx_number: '',
        phone_number: '',
        email: '',
        constellation: '',
        hobby: '',
        dream: '',
        graduation_message: '',
      };
    },
    async getai() {
      console.log('AI');
      console.log('graduation_message', this.formData.graduation_message);
      axios.get('/xunfei/semantic/textcreat', {
        params: {
          text: JSON.stringify(this.formData.graduation_message),
        }
      }).then(response => {
        // 处理成功响应
        if (response.status == 200) {
          console.log('response', response.data);
          this.formData.graduation_message = response.data;
          console.log('AI生成成功！', this.formData.graduation_message);

        } else {
          console.log('AI生成失败！');
        }
      }).catch(error => {
        // 处理错误响应
        console.error('ohuo:', error);
      });

    },
  },
  mounted() {
    this.editor = new EditorJS({
      // 在此配置EditorJS实例
      holder: 'editor', // 指定初始化Editor的容器ID
      // 根据需要添加任何其他配置选项
      autofocus: true,
      tools: {
        paragraph: {
          class: paragraph,//指定工具的类
          inlineToolbar: true,//是否显示行内工具栏
        }
      },
      onChange: () => {
        // 当编辑器内容发生变化时触发
        this.editor.save().then((outputData) => {
          // 将编辑器内容保存到数据库
          // this.formData.graduation_message = JSON.stringify(outputData);
          console.log(outputData);
          outputData.blocks.forEach((block) => {
            console.log('text', block.data.text);
            this.formData.graduation_message = block.data.text;
            console.log('graduation_message', this.formData.graduation_message);
          });
          console.log('保存成功', this.formData.graduation_message);
        }).catch((error) => {
          // 处理保存错误
          console.error('保存错误', error);
        });
      },

    });
  },
  beforeDestroy() {
    if (this.editor) {
      this.editor.destroy(); // 在组件销毁时销毁Editor实例
    }
  },
};
</script>
<style scoped>
.add-classmates {
  height: calc(100vh - 60px);
  width: 100%;
  overflow-y: auto;
  /* 当内容超出容器高度时，显示滚动条 */
}

.title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 42px;
}

.layout {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 20px;
}

.off {
  margin-top: 20px;
  display: grid;
  grid-template-rows: 1fr 1fr auto;
  grid-gap: 20px;
}

#editor {
  width: 100%;
  height: 200px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.avatar {
  grid-row: span 5;
}

.add-card {
  width: 70%;
  margin: 0 auto;
  padding: 20px;
  background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* 将输入框样式 */
.input {
  background-color: transparent;
  border: none;
}

/* 设置输入框获取焦点时的样式 */
.input:focus {
  outline: none;
  /* 移除焦点轮廓 */
  border-bottom-color: #a6b8fc;
  /* 改变底部边框颜色 */
}

/* 设置按钮样式 */
button {
  width: 100px;
  /* 设置宽度 */
  padding: 10px;
  /* 添加内边距 */
  margin: 10px;
  /* 添加外边距 */
  border: none;
  /* 移除边框 */
  border-radius: 5px;
  /* 设置圆角 */
  background-color: #c88dee;
  /* 设置背景颜色 */
  color: #fff;
  /* 设置字体颜色 */
  font-size: 16px;
  /* 设置字体大小 */
  cursor: pointer;
  /* 设置鼠标样式 */
}

/* 设置按钮悬停时的样式 */
button:hover {
  background-color: #a6b8fc;
  /* 改变背景颜色 */
}

/* 设置按钮激活时的样式 */
button:active {
  background-color: #b3a5fa;
  /* 改变背景颜色 */
}

/* 设置按钮禁用时的样式 */
button:disabled {
  background-color: #ccc;
  /* 改变背景颜色 */
  color: #666;
  /* 改变字体颜色 */
  cursor: not-allowed;
  /* 设置鼠标样式 */
}

/* 设置按钮获取焦点时的样式 */
button:focus {
  outline: none;
  /* 移除焦点轮廓 */
}

/* 设置按钮容器样式 */
.button {
  display: flex;
  /* 设置弹性布局 */
  justify-content: center;
  /* 设置主轴对齐方式 */
}
</style>