<template>
  <div class="login-wrap">
    <div class="ms-login">
      <div class="ms-title">Rocky的小作坊</div>
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="ms-content">
        <el-form-item prop="username">
          <el-input v-model="ruleForm.username" placeholder="username" clearable>
            <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" placeholder="password" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')" clearable>
            <el-button slot="prepend" icon="el-icon-lx-lock" ></el-button>
          </el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
        </div>
        <!-- <p class="login-tips">Tips : 用户名和密码随便填。</p> -->
      </el-form>
    </div>
  </div>
</template>

<script>
import img from "@/assets/20181123112006.jpg";
export default {
  name: "login",
  data: function() {
    return {
      ruleForm: {
        username: "",
        password: ""
      },
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" }
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          console.log("发起登录");
          this.$axios
            .post("/rocky/api-token-auth/", this.ruleForm)
            .then(response => {
              console.log(response);
              let token = response.data.token;
              this.$store.commit("set_token", "Token " + token);
              localStorage.setItem("ms_username", this.ruleForm.username);
              this.$router.push("/");
            })
            .catch(error => {
              // console.log(error);
              this.$toast("Invalid Usermane or Password !");
            });
        } else {
          // console.log('error submit!!');
          this.$toast("Invalid Usermane or Password !");
          return false;
        }
      });
    }
  }
};
</script>

<style>
#login_wrap {
  background-image: url("~@/assets/20181123112006.jpg");
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  background-position: center center;
  background-repeat: no-repeat;
}
.login-wrap {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image: url("~@/assets/20181123112006.jpg");
  background-size: 100%;
}
.ms-title {
  width: 100%;
  line-height: 50px;
  text-align: center;
  font-size: 20px;
  color: #fff;
  border-bottom: 1px solid #ddd;
}
.ms-login {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 350px;
  margin: -180px 0 0 -175px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.3);
  overflow: hidden;
}
.ms-content {
  padding: 30px 30px;
}
.login-btn {
  text-align: center;
}
.login-btn button {
  width: 100%;
  height: 36px;
  margin-bottom: 10px;
}
.login-tips {
  font-size: 12px;
  line-height: 30px;
  color: #fff;
}
</style>
