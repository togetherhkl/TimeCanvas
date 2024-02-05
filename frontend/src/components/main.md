//保存代码 主体下面 利用element-plus
<div class="main-off">
      <div class="on-space">
        <el-row :gutter="40">
          <el-col :span="4">
            <div class="grid-content ep-bg-purple" style="text-align: center;">
              <img src="../assets/1.png" style="width: 180px;height: 250px;" alt="趣事录">
              <p style="font-size: larger; align-items: center;">趣事录</p>
            </div>
          </el-col>
           <!--  <ul class="card-list"> -->
              <el-col :span="4">

              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>篮球</h2>
                </a>
              </li>
            </el-col>

            <el-col :span="4">
              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>足球</h2>
                </a>
              </li>
            </el-col>

            <el-col :span="4">
              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>羽毛球</h2>
                </a>
              </li>
            </el-col>

            <el-col :span="4">
              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>拔河</h2>
                </a>
              </li>
            </el-col>

            <!-- </ul> -->
          </el-row>

      </div>
    </div>


<!-- addinformation -->
<el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="150px" class="demo-ruleForm"
        :size="formSize" status-icon>
        <el-form-item label="同学录相册名称" prop="classmates_album_name">
          <el-radio-group v-model="ruleForm.classmates_album_name">
            <el-radio label="小学" />
            <el-radio label="初中" />
            <el-radio label="高中" />
            <el-radio label="大学" />
          </el-radio-group>
        </el-form-item>
        <el-form-item label="同学头像" prop="">
          <el-upload class="avatar-uploader" action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :show-file-list="false" :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <el-icon v-else class="avatar-uploader-icon">
              <Plus />
            </el-icon>
          </el-upload>
        </el-form-item>
        <el-col :span="12">
          <el-form-item label="姓名" prop="name">
            <el-input v-model="ruleForm.name" />
          </el-form-item>
        </el-col>
        <el-form-item label="昵称" prop="nickname">
          <el-input v-model="ruleForm.nickname" />
        </el-form-item>
        <el-form-item label="生日" required>
          <el-col :span="24">
            <el-form-item prop="birthday">
              <el-date-picker v-model="ruleForm.birthday" type="date" label="Pick a date" style="width: 100%" />
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="家乡" prop="hometown">
          <el-input v-model="ruleForm.hometown" />
        </el-form-item>
        <el-form-item label="爱好" prop="hobby">
          <el-checkbox-group v-model="ruleForm.hobby">
            <el-checkbox label="hobby.basketball" name="type">篮球</el-checkbox>
            <el-checkbox label="hobby.badminton" name="type">羽毛球</el-checkbox>
            <el-checkbox label="hobby.football" name="type">足球</el-checkbox>
            <el-checkbox label="hobby.jogging" name="type">跑步</el-checkbox>
            <el-checkbox label="hobby.chat" name="type">聊天</el-checkbox>
          </el-checkbox-group>
          <el-input v-model="additionalHobby" placeholder="请输入其他爱好"></el-input>
          <el-button @click="addHobby">添加爱好</el-button>
        </el-form-item>
        <el-form-item label="QQ" prop="qq_number">
          <el-input v-model="ruleForm.qq_number" />
        </el-form-item>
        <el-form-item label="微信" prop="wx_number">
          <el-input v-model="ruleForm.wx_number" />
        </el-form-item>
        <el-form-item label="手机号" prop="phone_number">
          <el-input v-model="ruleForm.phone_number" />
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="ruleForm.email" />
        </el-form-item>
        <el-form-item label="星座" prop="constellation">
          <el-select v-model="ruleForm.constellation" placeholder="Activity zone">
            <el-option label="白羊座" value="白羊座">
              <i class="iconfont icon-muyangzuo">白羊座</i>
            </el-option>
            <el-option label="金牛座" value="金牛座">
              <i class="iconfont icon-jinniuzuo">金牛座</i>
            </el-option>
            <el-option label="双子座" value="双子座">
              <i class="iconfont icon-shuangyuzuo">双子座</i>
            </el-option>
            <el-option label="巨蟹座" value="巨蟹座">
              <i class="iconfont icon-juxiezuo">巨蟹座</i>
            </el-option>
            <el-option label="狮子座" value="狮子座">
              <i class="iconfont icon-shizizuo">狮子座</i>
            </el-option>
            <el-option label="处女座" value="处女座">
              <i class="iconfont icon-chunvzuo">处女座</i>
            </el-option>
            <el-option label="天秤座" value="天秤座">
              <i class="iconfont icon-tianchengzuo">天秤座</i>
            </el-option>
            <el-option label="天蝎座" value="天蝎座">
              <i class="iconfont icon-tianhezuo">天蝎座</i>
            </el-option>
            <el-option label="射手座" value="射手座">
              <i class="iconfont icon-sheshouzuo">射手座</i>
            </el-option>
            <el-option label="摩羯座" value="摩羯座">
              <i class="iconfont icon-mojiezuo">摩羯座</i>
            </el-option>
            <el-option label="水瓶座" value="水瓶座">
              <i class="iconfont icon-shuipingzuo">水瓶座</i>
            </el-option>
            <el-option label="双鱼座" value="双鱼座">
              <i class="iconfont icon-muyangzuo">双鱼座</i>
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="梦想" prop="dream">
          <el-input v-model="ruleForm.dream" />
        </el-form-item>
        <el-form-item label="毕业寄语" prop="gradutaion_message">
          <el-input v-model="ruleForm.gradutaion_message" type="textarea" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm(ruleFormRef)">
            添加
          </el-button>
          <el-button @click="resetForm(ruleFormRef)">重置</el-button>
        </el-form-item>
      </el-form>