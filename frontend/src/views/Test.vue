<template>
  <el-upload :action="uploadAction" :file-list="fileList" :on-change="handleChange" :auto-upload="false"
    :multiple="true" :before-upload="handleChange" :on-remove="handleRemove" :http-request="handleFileUpload"
    ref="uploadMutiple" list-type="picture-card">
    <el-icon>
      <Plus />
    </el-icon>
  </el-upload>
  <el-button type="primary" @click="submitUpload">上传</el-button>
</template>

<script>
import axios from 'axios';
import { Plus } from '@element-plus/icons-vue'
import { getUserInfo, calculateMD5 } from '../assets/common/utils.js'

export default {
  data() {
    return {
      uploadAction: '',
      fileList: [],
      md5: ''
    };
  },
  methods: {
    test() {
      const userinfo = getUserInfo();
      userinfo.then(res => {
        console.log(res[0]);
      });
    },
    // 上传文件改变时的状态，打印选择的文件的文件信息
    /**
  * 文件上传change
  */
    handleChange(file, fileList) {
      // console.log("文件改变了")
      // console.log(file);
      // console.log(fileList);
      this.fileList = fileList;
    },
    handleRemove(file, fileList) {
      console.log("文件移除")
      console.log(file, fileList);
    },
    handleBeforeUpload(file) {
      console.log("打印文件大小")
      console.log(file.size); // 打印文件大小
      return false; // 阻止文件自动上传
    },
    beforeUpload(file) {
      // console.log(file);
    },
    handleFileUpload(data) {
      console.log("文件上传")
      console.log(data);
      //百度网盘预上传
      //获取文件大小
      const file = data.file;
      calculateMD5(file).then(res => {
        let md5 = res;



        console.log('list');
        const list = []
        list.push(md5);
        console.log(list);
        const path = "/apps/TimeGallery/test" + data.file.name;
        const encodedPath = encodeURIComponent(path);


        //获取文件的md5值
        const url = "http://pan.baidu.com/rest/2.0/xpan/file?method=precreate&access_token=121.2b64b0b989618096f6418245851698cd.Y_xqR97cR1gf86XMBm8KQjCwk5Hq7zsLphJUfAO.u3sOAw"
        axios.post(url, {
          filename: data.file.name,
          size: data.file.size,
          isdir: 0,
          block_list: list,
          path: encodedPath
        },
          {
            headers: {
              'User-Agent': 'pan.baidu.com'
            }
          }).then(res => {
            console.log(res);
          }).catch(err => {
            console.log(err);
          });
      });
    },
    submitUpload() {
      this.$refs.uploadMutiple.submit();
    }
  }
}
</script>