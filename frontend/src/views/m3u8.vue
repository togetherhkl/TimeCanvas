<template>
    <h1>m3u8视频播放器
    </h1>
    <div>
      <video ref="videoPlayer" class="video-js vjs-default-skin" controls width="800px" crossOrigin="anonymous">
        <source :src="videoSrc" type="application/x-mpegURL">
      </video>
    </div>
  </template>
  
  <script>
  import videojs from 'video.js';
  import 'video.js/dist/video-js.css';
  import axios from 'axios';
  
  export default {
    mounted() {
      // Initialize the video player
      // console.log("加载视频")
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
      //       this.videoSrc = response.data
      //       this.player = videojs(this.$refs.videoPlayer, {}, function() {
      //       console.log('Video player is ready');
      // });
      //   })
      this.player = videojs(this.$refs.videoPlayer, {}, function() {
            console.log('Video player is ready');
      });
    },
    data() {
      return {
        // videoSrc: 'https://v1-ant.baidu.com/video/netdisk-videotran-yangquan/55d397eb6l3d5621b3025eab3d83b9ac_1138_1_ts/faff93dd88af5992b021452860b4a27b?ts_size=5599956&app_id=45762545&csl=130&dp-logid=3636491147214601&fn=test.mp4&from_type=3&fsid=30489994932995&iot_dev=0&iot_vip=0&iv=0&logid=3636491147214601&mtime=1703728620&ouk=2867615989&r=136753544&size=77730829&sta_cs=11001&sta_dt=video&sta_dx=74&time=1712670681&to=vas1&tot=cn1v7&uo=cnc&uva=3432552396&vuk=2867615989&dtime=10&etag=faff93dd88af5992b021452860b4a27b&fid=a034e43528a29f26699a99919057d96d-2867615989&len=248912&range=194956-443867&region=yangquan&resv4=&sign=BOUTRFPQV-F3530edecde9cd71b79378b290804a96-Q0t60DBt7TANstZ5EKhguu2Gv%252FY%253D&xcode=90ca31a57259b8a3d49fde4bf887ad4f915494224a4cbc9e3cc3c8a7fc538f31f982bf25f77b80a2e3968bccc71c05382ab563967f9645c3&xv=6&need_suf=&pmk=1400faff93dd88af5992b021452860b4a27be3a6395c0000005572d4&by=my-streaming.m3u8'
        videoSrc: 'https://pan.baidu.com/rest/2.0/xpan/file?method=streaming&access_token=121.82082f731c029b7aaab1b92ccc744e1b.YmlJx6oXvQai-a-1deV1_XQ2kNLX0p5qggofBRD.FgKv4g&path=%E5%AD%A6%E4%B9%A0%E8%A7%82/test.mp4&type=M3U8_AUTO_480&adToken=hMo8Nsj7CntDmTBPnFOgK8iSB5j2z3CAs5FPVBGHNQbqLUDkiHEWB23K/xiSliTfwDCSwB9QOpKLyO6WERIkWs72mqFKWz%2BoSYLPk8jwLdnaR9vjkRp7CkWd1GyB6uYuGlhSJ3Bit3vfaC2SXX3s%2BA%3D%3D'
        // videoSrc:'http://devimages.apple.com/iphone/samples/bipbop/gear1/prog_index.m3u8'
        
      };
      //http://127.0.0.1:8000/
      //https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8
    },
    beforeDestroy() {
      // Dispose of the video player when the component is destroyed
      if (this.player) {
        this.player.dispose();
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any custom styles here */
  </style>
  