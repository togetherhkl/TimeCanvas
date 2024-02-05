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

  <template>
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
  
  