<template>
    <div class="login-wrap">
        <van-cell-group>
            <van-field v-model="ruleForm.username" required clearable label="用户名" placeholder="请输入用户名" />
            <van-field v-model="ruleForm.password" type="password" label="密码" placeholder="请输入密码" required />
            <br>
            <van-button type="default" size="small" :click="submitForm(ruleForm)">Do Login</van-button>
        </van-cell-group>
    </div>
</template>

<script>
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
      if (true) {
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
          });
      } else {
        // console.log('error submit!!');
        this.$toast("ERROR: Invalid Usermane or Password !");
        return false;
      }
    }
  }
};
</script>
