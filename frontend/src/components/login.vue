<template>
    <div style="margin-top:10%; margin:10% auto;width:20%; ">
<el-form :inline="false" :model="formInline" :rules="rules" ref="formInline" >
  <el-form-item prop="user">
    <el-input v-model="formInline.user" placeholder="Username"></el-input>
  </el-form-item>
  <el-form-item prop="password">
    <el-input v-model="formInline.password" placeholder="Password" type="password"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button style="width: 100%" type="primary" @click="handleSubmit('formInline')">登录</el-button>
  </el-form-item>
</el-form>
    </div>
</template>

<script type="text/javascript">
import $ from 'jquery'
export default {
    name: 'login',
    data(){
        return {
            formInline: {
                user: '',
                password: ''
            },
            rules: {
                user: [
                    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
                    { min: 5, max: 16, message: '长度在 5 到 16 个字符', trigger: 'blur' }
                ],
                password: [
                    { required: true, message: '请输入密码', trigger: 'blur' },
                    { min: 5, max: 16, message: '长度在 5 到 16 个字符', trigger: 'blur' }
                ]
            },
            ruleInline: {
                user: [
                    { required: true, message: 'Please fill in the user name', trigger: 'blur' }
                ],
                password: [
                    { required: true, message: 'Please fill in the password.', trigger: 'blur' },
                    { type: 'string', min: 6, message: 'The password length cannot be less than 6 bits', trigger: 'blur' }
                ]
            }
        }
    },
    methods: {
    	sendPost(){
            var token =  ""
            var postuser = {
            	username : this.formInline.user, 
            	password : this.formInline.password
            }
            // console.log(postuser);
            var _this = this
            var myrouter = this.$router
            var mystore = this.$store
            $.ajax({
                url:"/api-token-auth/",
                type:'POST',
                data : postuser,
                success: function(data) {
                    console.log('Login Success!')
                    token = data.token
                    mystore.commit('set_token',"Token "+ token)
                    myrouter.push({path :'/dashboard' })
                },
                error: function() {
                    _this.$message.error('ERROR: Invalid Usermane or Password !')
                    // console.log('Login Faild!')
                }
            })  
        },
        handleSubmit(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.sendPost()                    
                } else {
                    this.$message.error('ERROR: Invalid Usermane or Password !')
                }
            })
        }
    }
}
</script>

<style scoped>
.p-color {
	color: red;
}
</style>
