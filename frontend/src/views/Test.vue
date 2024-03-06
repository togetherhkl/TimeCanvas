<!-- <template>
  <el-button text @click="centerDialogVisible = true">
    Click to open the Dialog
  </el-button>

  <el-dialog
    v-model="centerDialogVisible"
    title="Warning"
    width="30%"
    align-center
  >
    <span>Open the dialog from the center from the screen</span>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="centerDialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="centerDialogVisible = false">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<script lang="ts" setup>
import { ref } from 'vue'

const centerDialogVisible = ref(false)
</script>
<style scoped>
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style> -->
<!-- <template> <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/psychopomp-500.jpg"
  @click="$router.push('/home/primary')" alt="primary" />
  <i class="iconfont icon-muyangzuo">白羊座</i>

  </template> -->

<!--   <template>
    <div>
      <el-form :model="form" label-width="100px">
        <el-form-item label="请选择爱好：">
          <el-checkbox-group v-model="form.hobbies">
            <el-checkbox label="篮球"></el-checkbox>
            <el-checkbox label="足球"></el-checkbox>
            <el-checkbox label="游泳"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="输入新爱好：">
          <el-input v-model="newHobby"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="addNewHobby">添加</el-button>
        </el-form-item>
      </el-form>
      <p>已选爱好: {{ form.hobbies }}</p>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { ElForm, ElFormItem, ElCheckboxGroup, ElCheckbox, ElInput, ElButton } from 'element-plus';
  
  const form = ref({
    hobbies: [] as string[]
  });
  const newHobby = ref('');
  
  const addNewHobby = () => {
    if (newHobby.value) {
      form.value.hobbies.push(newHobby.value);
      newHobby.value = '';
    }
  };
  </script>
   -->
   <template>
    <div>
        <el-dialog title="创建趣事录" :visible.sync="dialogVisible" :close-on-click-modal="false">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="趣事录名称">
                    <el-input v-model="form.eventName" placeholder="请输入趣事录名称"></el-input>
                </el-form-item>
                <el-form-item label="趣事录封面图">
                    <el-upload
                        class="upload-demo"
                        action="/api/create-interesting-event"
                        :on-success="handleUploadSuccess"
                        :on-error="handleUploadError"
                        :before-upload="beforeUpload"
                        :auto-upload="false"
                        :file-list="fileList"
                        :limit="1"
                        :show-file-list="false"
                    >
                        <el-button slot="trigger" size="small" type="primary">点击上传</el-button>
                        <el-tooltip class="item" effect="dark" content="上传封面图" placement="top">
                            <i class="el-icon-picture-outline"></i>
                        </el-tooltip>
                    </el-upload>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="submitForm">提 交</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
export default {
    data() {
        return {
            dialogVisible: false,
            form: {
                eventName: '',
                photo: null
            },
            fileList: []
        };
    },
    methods: {
        handleUploadSuccess(response, file, fileList) {
            // Handle success response
            console.log(response);
        },
        handleUploadError(error, file, fileList) {
            // Handle error response
            console.error(error);
        },
        beforeUpload(file) {
            // Validate file type and size
            const isJPG = file.type === 'image/jpeg';
            const isPNG = file.type === 'image/png';
            const isLt2M = file.size / 1024 / 1024 < 2;

            if (!isJPG && !isPNG) {
                this.$message.error('只能上传 JPG/PNG 格式的图片');
            }
            if (!isLt2M) {
                this.$message.error('上传图片大小不能超过 2MB');
            }

            return (isJPG || isPNG) && isLt2M;
        },
        submitForm() {
            this.$refs.form.validate(valid => {
                if (valid) {
                    // Perform API call to send eventName and photo to the backend
                    // Example using axios:
                    const formData = new FormData();
                    formData.append('eventName', this.form.eventName);
                    formData.append('photo', this.form.photo);

                    axios.post('/api/create-interesting-event', formData)
                        .then(response => {
                            // Handle success response
                            console.log(response.data);
                        })
                        .catch(error => {
                            // Handle error response
                            console.error(error);
                        });
                } else {
                    return false;
                }
            });
        }
    }
};
</script>