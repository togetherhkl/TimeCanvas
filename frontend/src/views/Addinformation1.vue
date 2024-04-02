<template>
  <div class="add-classmates">
    <div class="add-card">
      <div class="title">时光卡片</div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="classmates_album_name">时光回溯</label>
          <input type="radio" id="primary" name="classmates_album_name" value="primary"
            v-model="formData.classmates_album_name">
          <label for="primary">小学</label>
          <input type="radio" id="middle" name="classmates_album_name" value="junior"
            v-model="formData.classmates_album_name">
          <label for="middle">初中</label>
          <input type="radio" id="high" name="classmates_album_name" value="senior"
            v-model="formData.classmates_album_name">
          <label for="high">高中</label>
          <input type="radio" id="university" name="classmates_album_name" value="university"
            v-model="formData.classmates_album_name">
          <label for="university">大学</label>
        </div>
        <div class="layout">
          <div>
            <label for="name">姓名:</label>
            <input type="text" id="name" v-model="formData.name" required>
          </div>
          <div>
            <label for="nickname">昵称:</label>
            <input type="text" id="nickname" v-model="formData.nickname">
          </div>
          <div class="avatar">
            <label for="classmates_avatar_name">头像</label>
            <input id="classmates_avatar_name" v-model="formData.classmates_avatar_name">

           <!--  <input type="file" id="classmates_avatar_name" accept="image/*" @change="handleAvatarChange">
            <img v-if="avatarPreview" :src="avatarPreview" alt="Avatar Preview"
              style="max-width: 200px; max-height: 200px;"> -->
          </div>
          <div>
            <label for="birthday">生日:</label>
            <input type="date" id="birthday" v-model="formData.birthday">
          </div>
          <div>
            <label for="hometown">家乡:</label>
            <input type="text" id="hometown" v-model="formData.hometown">
          </div>
          <div>
            <label for="qq">QQ:</label>
            <input type="text" id="qq_number" v-model="formData.qq_number">
          </div>
          <div>
            <label for="wx_number">微信:</label>
            <input type="text" id="wx_number" v-model="formData.wx_number">
          </div>
          <div>
            <label for="phone">手机号:</label>
            <input type="text" id="phone_number" v-model="formData.phone_number">
          </div>
          <div>
            <label for="email">邮箱:</label>
            <input type="email" id="email" v-model="formData.email">
          </div>
          <div>
            <label for="constellation">星座:</label>
            <select style="width: 60%;" id="constellation" v-model="formData.constellation">
              <option value="白羊座">白羊座</option>
              <option value="金牛座">金牛座</option>
              <option value="双子座">双子座</option>
              <option value="巨蟹座">巨蟹座</option>
              <option value="狮子座">狮子座</option>
              <option value="处女座">处女座</option>
              <option value="天秤座">天秤座</option>
              <option value="天蝎座">天蝎座</option>
              <option value="射手座">射手座</option>
              <option value="摩羯座">摩羯座</option>
              <option value="水瓶座">水瓶座</option>
              <option value="双鱼座">双鱼座</option>
            </select>
          </div>
        </div>
        <div class="hobby">
          <label for="hobby">爱好:</label>
          <input type="text" id="hobby" v-model="formData.hobby">
        </div>
        <div class="mengxiang">
          <label for="dream">梦想:</label>
          <textarea id="dream" v-model="formData.dream"></textarea>
        </div>
        <div class="biyejiyu">
          <label for="graduation_message">毕业寄语:</label>
          <textarea id="graduation_message" v-model="formData.graduation_message"></textarea>
        </div>
        <button type="submit">确认</button>
        <button type="button" @click="resetForm">重置</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
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
        graduation_message: ''
      },
      avatarPreview: ''
    };
  },
  methods: {
    handleAvatarChange(event) {
      this.formData.classmates_avatar_name = event.target.files[0];
      this.avatarPreview = URL.createObjectURL(event.target.files[0]);
    },
    submitForm() {
      // 在这里将表单数据传到后端
      console.log(this.formData);
      console.log(this.formData.classmates_avatar_name);
      /* 如果表单为空，则返回；不为空，则将数据发送给数据库 */
      if (!this.formData) return;
      axios.post('/classmate/', this.formData)
        .then(response => {
          // 处理成功响应
          console.log(response.data);
        })
        .catch(error => {
          // 处理错误响应
          console.error(error);
        });
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
        graduation_message: ''
      };
    }
  }
};
</script>
<style scoped>
.add-classmates {
  height: 100vh;
  widows: 100%;
  /* 虚化背景 */
  backdrop-filter: brightness(0.5);
  /* background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee); */
  overflow-y: auto;
}
.title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 42px;
  color: white;
}

.layout {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}

.avatar {
  grid-row: span 5;
}

.hobby input,
.mengxiang textarea,
.biyejiyu textarea {
  width: 100%;
  /* 让输入框宽度占满父元素的宽度 */
  height: 100px;
  font-size: 16px;
}

.add-card {
  width: 70%;
  margin: 0 auto;
  padding: 20px;
  /* background-color: #cdd1d3; */
  background-image: linear-gradient(to right top, #6cb5e4, #00c9ef, #00dce3, #00eabf, #57f489);
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-row {
  display: flex;
  justify-content: space-between;
}

.add-card form div {
  margin-bottom: 10px;
}

.add-card form div label {
  display: inline-block;
  width: 100px;
  color: white;
}

.add-card form div input {
  font-size: 16px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
  background: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.add-card form div select {
  font-size: 16px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
  background: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.add-card form div textarea {
  font-size: 16px;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
  background: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.add-card form button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  border: none;
  background: #409EFF;
  color: white;
  cursor: pointer;
}

.add-card form button:active {
  background: #66b1ff;
}

.add-card form button:hover {
  background: #3a8ee6;
}

.add-card form button+button {
  margin-left: 20px;
}
</style>