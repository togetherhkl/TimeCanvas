<template>
  <!-- <iframe src="https://www.cnblogs.com/ggband/p/10848803.html" width="800" height="600"></iframe> -->
    <div class="test-videojs">
      <video id="videoPlayer" class="video-js" muted crossOrigin="anonymous"></video>
    </div>
  </template>
  <script>
  import Videojs from "video.js"; // 引入Videojs 
  import axios from "axios";

  export default {
    data() {
      return {
      //  https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8 是一段视频，可将cctv1 （是live现场直播，不能快退）的替换为它，看到快进快退的效果
        nowPlayVideoUrl: "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
        // nowPlayVideoUrl:"./assets/test.m3u8"
      };
    },
    mounted() {
        // axios.get('http://localhost:8000/baidufile/m3u8',{
        //     headers: {
        //       'Content-Type': 'application/x-mpegURL',
        //     },
        //     params:{
        //       "path":"学习观/test.mp4"
    
        //     }
          
        //   })
        //   .then(response =>{
        //       console.log(response.data)
        //       this.nowPlayVideoUrl = response.data
        //       this.initVideo(this.nowPlayVideoUrl);
        //   })
      this.initVideo(this.nowPlayVideoUrl);
      
    },
    methods: {
      initVideo(nowPlayVideoUrl) {
        // 这些options属性也可直接设置在video标签上，见 muted
        let options = {
          autoplay: true, // 设置自动播放
          controls: true, // 显示播放的控件
          sources: [
            // 注意，如果是以option方式设置的src,是不能实现 换台的 (即使监听了nowPlayVideoUrl也没实现)
            {
              src: nowPlayVideoUrl,
              type: "application/x-mpegURL" // 告诉videojs,这是一个hls流
            }
          ]
        };
        // videojs的第一个参数表示的是，文档中video的id
        const myPlyer = Videojs("videoPlayer", options, function onPlayerReady() {
          console.log("onPlayerReady 中的this指的是：", this); // 这里的this是指Player,是由Videojs创建出来的实例
          console.log(myPlyer === this); // 这里返回的是true
        });
      }
    }
  };
  </script>
  <style>
  #videoPlayer {
    width: 500px;
    height: 300px;
    margin: 50px auto;
  }
  </style>