<template>
    <div style="margin-top:10%; margin:10% auto;width:20%; " >
<el-form :inline="false" :model="formInline" :rules="rules" ref="formInline"
    @keyup.enter.native="handleSubmit('formInline')"  >
  <el-form-item prop="user">
    <el-input v-model="formInline.user" placeholder="Username"></el-input>
  </el-form-item>
  <el-form-item prop="password">
    <el-input v-model="formInline.password" placeholder="Password" type="password"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button style="width: 100%" type="primary" 
    @click="handleSubmit('formInline')">登录</el-button>
  </el-form-item>
</el-form>
    </div>
</template>

<script type="text/javascript">
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      formInline: {
        user: "",
        password: ""
      },
      rules: {
        user: [
          { required: true, message: "请输入邮箱地址", trigger: "blur" },
          { min: 5, max: 16, message: "长度在 5 到 16 个字符", trigger: "blur" }
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 5, max: 16, message: "长度在 5 到 16 个字符", trigger: "blur" }
        ]
      },
      ruleInline: {
        user: [
          {
            required: true,
            message: "Please fill in the user name",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            message: "Please fill in the password.",
            trigger: "blur"
          },
          {
            type: "string",
            min: 6,
            message: "The password length cannot be less than 6 bits",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    sendPost() {
      var token = "";
      var postuser = {
        username: this.formInline.user,
        password: this.formInline.password
      };
      // console.log(postuser);
      var _this = this;
      var myrouter = this.$router;
      // 获取Vuex store
      var mystore = this.$store;

      axios({
        method: "POST",
        url: "/api-token-auth/",
        data: JSON.stringify(postuser),
        headers: { Authorization: token }
      }).then(response => {
        // console.log(response)
        // callback(response.data)
        token = response.data.token;
        // 通过Vuex 设置token
        mystore.commit("set_token", "Token " + token);
        myrouter.push({ path: "/dashboard" });
      });

      $.ajax({
        url: "/api-token-auth/",
        type: "POST",
        data: postuser,
        success: data => {
          console.log("Login Success!");
          token = data.token;
          // 通过Vuex 设置token
          mystore.commit("set_token", "Token " + token);
          myrouter.push({ path: "/dashboard" });
        },
        error: () => {
          _this.$message.error("ERROR: Invalid Usermane or Password !");
        }
      });
    },
    handleSubmit(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.$cookies.set(
            "formInline",
            JSON.stringify(this.formInline),
            60 * 60 * 24 * 7
          );
          // console.log(this.$cookies.get('formInline'))
          this.sendPost();
        } else {
          this.$message.error("ERROR: Invalid Usermane or Password !");
        }
      });
    }
  },
  created: function() {
    let _this = this;
    if (_this.$cookies.isKey("formInline")) {
      // console.log(this.$cookies.keys() )
      // console.log(this.$cookies.get("formInline") )
      this.formInline = JSON.parse(this.$cookies.get("formInline"));
    }
  }
};
</script>

<style scoped>
.p-color {
  color: red;
}
</style>
