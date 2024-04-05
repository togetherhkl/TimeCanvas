<template>
  <div class="home">
    <div class="bookshelf" v-loading="loading">
      <div class="book" v-for="item in albuminfo">
        <el-image @click="openInNewTab(item.albumtype_id,item.albumtype_name)" :src="item.albumtype_cover" style="width: 100%;height: 100%;"
          fit='cover' :crossorigin="null"/>
        <h1 class="albumtype_name">{{ item.albumtype_name }}</h1>
        <p class="albumtype_description">{{ item.albumtype_description }}</p>
        <el-button class="button" @click="openInNewTab(item.albumtype_id,item.albumtype_name)" type="primary">阅读</el-button>
      </div>
    </div>
  </div>
</template>

<script>
//import { Loading } from 'element-plus/es/components/loading/src/service';
import axios from 'axios';
export default {
  data() {
    return {
      albuminfo: [],//相册信息
      loading: true,//加载动画
    }
  },
  methods: {
    // readBook(title) {
    //   if (title == '同学录')
    //     this.$router.push({ path: '/album', query: { id: 1 } });
    //   if (title == '趣事录')
    //     this.$router.push({ path: '/album', query: { id: 2 } });
    //   if (title == '旅游志')
    //     this.$router.push({ path: '/album', query: { id: 3 } });
    // }
    openInNewTab(id,album) {
      const url = this.$router.resolve({ path: 'album', query: { id: id, album: album } }).href;
      window.open(url, '_blank');
    }
  },
  mounted() {
    if (localStorage.getItem('timecanvas_token') == null) {
      this.$message.error('请先登录');
    } else {
      axios.get('/albuminfo').then(
        response => {
          if (response.status == 200) {
            this.albuminfo = response.data;
            console.log("akbumtype里的albuminfo", this.albuminfo);
            this.loading = false;//关闭加载动画
          }
        },
      );
    }
  },
}
</script>

<style scoped>
.bookshelf {
  display: flex;
  justify-content: center;
  height: 100%;
  padding-top: 50px;
  position: relative;
}
.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.book {
  position: relative;
  width: 400px;
  height: 600px;
  margin: 0 30px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  cursor: pointer;
}
.book:hover {
  transform: translateY(-10px) scale(1.05);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);/* 鼠标悬浮时的阴影效果 */
}
.albumtype_name {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 40px;
  font-weight: bold;
  text-align: center;
}

.albumtype_description {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 20px;
  text-align: center;
}

.button {
  position: absolute;
  bottom: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s;
}
</style>