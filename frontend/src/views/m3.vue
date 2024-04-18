<template>
  <div>
    <video ref="videoPlayer" controls width="500px"></video>
  </div>
  <div>
    <video src="http://localhost:8000/videostream/20240417104024503059_2867615989_sea.mp4" width="500px" controls="controls"></video>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      videoUrl: ''
    };
  },
  async mounted() {
    const response = await axios.get('http://localhost:8000/videostream/20240417104024503059_2867615989_sea.mp4', {
      responseType: 'blob'
    });
    this.videoUrl = URL.createObjectURL(response.data);
    this.$refs.videoPlayer.src = this.videoUrl;
    this.$refs.videoPlayer.addEventListener('loadedmetadata', () => {
      this.$refs.videoPlayer.play();
    });
  }
};
</script>