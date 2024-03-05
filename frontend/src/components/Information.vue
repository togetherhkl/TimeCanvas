<template>
    <div class="information-container">
        <div class="classmate-image">
            <img :src="classmates_avatar_name" style="width: 170px; height: 200px; margin: 20px;border-radius: 50%;" alt="同学录头像">
        </div>
        <div class="information">
            <div class="label">
                <i class="iconfont icon-xingming"></i>
                姓名
            </div>
            <div class="box">{{ name }}</div>
            <div class="label">
                <i class="iconfont icon-nicheng"></i>
                昵称
            </div>
            <div class="box">{{ nickname }}</div>
            <div class="label">
                <i class="iconfont icon-shengrix"></i>
                生日
            </div>
            <div class="box">{{ birthday }}</div>
            <div class="label">
                <i class="iconfont icon-jiaxiang"></i>
                家乡
            </div>
            <div class="box">{{ hometown }}</div>
            <div class="label">
                <i class="iconfont icon-ziyuan25"></i>
                爱好
            </div>
            <div class="box">{{ hobby }}</div>
            <div class="label">
                <i class="iconfont icon-QQ"></i>
                QQ
            </div>
            <div class="box">{{ qq_number }}</div>
            <div class="label">
                <i class="iconfont icon-weixin"></i>
                微信
            </div>
            <div class="box">{{ wx_number }}</div>
            <div class="label">
                <i class="iconfont icon-shouji"></i>
                手机
            </div>
            <div class="box">{{ phone_number }}</div>
            <div class="label">
                <i class="iconfont icon-youxiang"></i>
                邮箱
            </div>
            <div class="box">{{ email }}</div>
            <div class="label">
                <i class="iconfont icon-xingzuo"></i>
                星座
            </div>
            <div class="box">{{ constellation }}</div>
        </div>
        <div class="left-off">
            <div class="mengxiang-label">
                <i class="iconfont icon-mengxiang"></i>
                <span style="writing-mode: vertical-rl;">梦</span>
                <span style="writing-mode: vertical-rl;">想</span>
            </div>
            <div class="mengxiang-box">{{ dream }}</div>
        </div>
        <div class="right-off"></div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      name: '',
      nickname: '',
      birthday: '',
      hometown: '',
      hobby: '',
      qq_number: '',
      wx_number: '',
      phone_number: '',
      email: '',
      constellation: '',
      dream: '',
      id:'',
      classmates_album_name:'',
      classmates_avatar_name:'',
    };
  },
  created() {
    // 假设后端API的URL为 http://your-backend-api-url/classmateInfo
    axios.get('/classmate/senior')
      .then(response => {
        console.log(response)
        const temp = response.data['classmates']; // 假设后端返回的是一个包含同学信息的对象
        const classmateData = temp[0];
        this.name = classmateData.name;
        this.nickname = classmateData.nickname;
        this.birthday = classmateData.birthday;
        this.hometown = classmateData.hometown;
        this.hobby = classmateData.hobby;
        this.qq_number = classmateData.qq_number;
        this.wx_number = classmateData.wx_number;
        this.phone_number = classmateData.phone_number;
        this.email = classmateData.email;
        this.constellation = classmateData.constellation;
        this.dream = classmateData.dream;
        this.classmates_avatar_name = classmateData.classmates_avatar_name;
        console.log(classmateData);
      })
      .catch(error => {
        console.error('Error fetching classmate information', error);
      });
  }
};
</script>

<style scoped>
.information-container {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 3fr;

    .left-off {
        grid-column: 1/3;
        display: grid;
        grid-template-columns: 1fr 17fr;
    }

    .right-off {
        display: none;
    }
}
.information {
    display: grid;
    grid-template-columns: 1fr 2.5fr 1fr 2.5fr;

}

.label {
    height: 20px;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
}
.box {
    height: 20px;
    padding: 10px;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow:inset 0 0 6px rgba(255, 255, 255, 0.2);
}
.mengxiang-label {
    height: auto;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
    writing-mode: vertical-rl;
}
.mengxiang-box {
    padding: 10px;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow:inset 0 0 6px rgba(255, 255, 255, 0.2);
}
</style>