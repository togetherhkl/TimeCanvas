<template>
  <div class="main" v-loading="loading">
    <div class="title">
      <h1 class="title">{{ albumtype.albumtype_name }}</h1>
    </div>
    <el-row :gutter="24">
      <el-col :span="24">
        <ul class="card-list">
          <li class="card" v-for="tmp in album">
            <!-- <el-image style="width: 100%; height: 100%" :src=tmp.album_cover fit="cover"
              @click="$router.push({ path: `/${albumtype.albumtype_name}/informshow`, query: { stage: tmp.album_name } })"
              :crossorigin="null" /> -->

              <el-image style="width: 100%; height: 100%" :src=tmp.album_cover fit="cover"
              @click="openAlbum(albumtype.albumtype_name,tmp.album_name)"
              :crossorigin="null" />

            <a class="card-description" @click="openInNewTab(albumtype.albumtype_name,tmp.album_name)">
              <h2>{{ tmp.album_name }}</h2>
            </a>
          </li>
        </ul>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { ElMessage } from 'element-plus';
import axios from 'axios';
export default {
  data() {
    return {
      album: [],//相册类型内信息
      albumtype: [],//相册类型
      id: null,
      loading: true,
    }
  },
  //在页面加载时获取数据
  async created() {
    this.id = this.$route.query.id;
  },
  mounted() {
    //判断用户是否登录
    if (localStorage.getItem('timecanvas_token') == null) {
      ElMessage.error('请先登录');
    }
    else {
      //检测浏览器本地会话中是否有image_url
      // if(localStorage.getItem('image_url') != null){
      //   /* 删除本地会话 */
      //   localStorage.removeItem('image_url');
      //   this.image_url = JSON.parse(sessionStorage.getItem('image_url'));
      //   for (let i = 0; i < this.image_url.length; i++) {
      //     this.album.push({albumtype_cover:this.image_url[i]});
      //   }
      //   //this.albuminfo = this.image_url;
      //   console.log('if里的albu',this.album);
      //   this.loading = false;
      // }else{
      //从后端获取相册信息
      axios.get('/albuminfo').then(
        response => {
          if (response.status == 200) {
            let temp=[];//定义一个列表
            temp = response.data;
            console.log('album里返回的数据temp', temp);
            // console.log(this.albuminfo);
            // console.log(this.albuminfo[0]);
            // console.log(this.albuminfo[0].albumtype_cover);
            // for (let i = 0; i < this.albuminfo.length; i++) {
            //   this.image_url.push(this.albuminfo[i].albumtype_cover);
            // }
            // console.log(this.image_url);
            /* 将image_url放在浏览器本地会话中 */
            // localStorage.setItem('image_url', JSON.stringify(this.image_url));
            this.albumtype = response.data[this.id - 1];//获取相册类型

            this.album = temp[this.id - 1].album_list;
            console.log('album里的album', this.album);
            this.loading = false;
          }
        }
      )
      // }
    }
  },
  methods: {
    //打开新标签页
    openInNewTab(albumtype_name,album_name) {
      if(albumtype_name == '趣事录'){
        const url = this.$router.resolve({ path: `/interestingevents/informshow`, query: { stage: album_name} }).href;
        window.open(url, '_blank');
      }else if(albumtype_name=='旅游志'){
        const url = this.$router.resolve({ path: `/travels/informshow`, query: { stage: album_name} }).href;
        window.open(url, '_blank');
      }else if(albumtype_name=='同学录'){
        const url = this.$router.resolve({ path: `/classmates/informshow`, query: { stage: album_name} }).href;
        window.open(url, '_blank');
      }
      // const url = this.$router.resolve({ path: `/${albumtype_name}/informshow`, query: { stage: album_name} }).href;
      // window.open(url, '_blank');
    },
    //打开相册
    openAlbum(albumtype_name,album_name){
      if(albumtype_name == '趣事录'){
        this.$router.push({ path: '/interestingevents/informshow', query: { stage:album_name } });
      }else if(albumtype_name=='旅游志'){
        this.$router.push({ path: '/travels/informshow', query: { stage:album_name } });
      }else if(albumtype_name=='同学录'){
        this.$router.push({ path: '/classmates/informshow', query: { stage:album_name } });
      }
    }
  },
}

</script>

<style scoped>
.main {
  width: 100vw;
  height: 100vh;
}
.title {
  text-align: center;
  margin-top: 20px;
  font-size: 40px;
  text-align: center;
}
.card-image {
  display: block;
  min-height: 230px;
  background: #fff center center no-repeat;
  background-size: cover;
  width: 100%;
}
.card-image>img {
  display: block;
  width: 100%;
  height: 100%;
  opacity: 1;
  object-fit: cover;
}
.card-list {
  display: flex;
  margin: 0 auto;
  padding: 0;
  font-size: 0;
  text-align: center;
  list-style: none;
}
.card {
  display: flex;
  flex-direction: column;
  width: 200px;
  height: 300px;
  max-width: 20rem;
  margin: 0 1rem auto;
  font-size: 1rem;
  text-decoration: none;
  overflow: hidden;
  box-shadow: 0 0 3rem -1rem rgba(0, 0, 0, 0.5);
  transition: transform 0.1s ease-in-out, box-shadow 0.1s;
}
.card:hover {
  transform: translateY(-0.5rem) scale(1.0125);
  box-shadow: 0 0.5em 3rem -1rem rgba(0, 0, 0, 0.5);
}
.card-description {
  display: block;
  padding: 1em 0.5em;
  color: #515151;
  text-decoration: none;
}
.card-description>h2 {
  margin: 0 0 0.5em;
}
</style>