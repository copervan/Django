<template>
    <Form ref="formInline" :model="formInline" :rules="ruleInline" inline>
        <FormItem prop="user">
            <Input type="text" v-model="formInline.user" placeholder="Username">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <FormItem prop="password">
            <Input type="password" v-model="formInline.password" placeholder="Password">
                <Icon type="ios-locked-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('formInline')">Sign In</Button>
        </FormItem>
        <!-- <p class="p-color" >{{formInline.user}}</p> -->
        <!-- <p class="p-color" >{{formInline.password}}</p>  -->
    </Form>
</template>

<script>
	import $ from 'jquery';
    // import  from 'vue-router'
    import dashboard from './dashboard'
    //import store from './store'
    export default {
    	name: 'login',
        data () {
            return {
                formInline: {
                    user: '',
                    password: ''
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
	            console.log(postuser);

                var myrouter = this.$router
                var mystore = this.$store
                $.ajax({
                    url:"/api-token-auth/",
                    type:'POST',
                    data : postuser,
                    success: function(data) {
                        console.log('Login Success!')
                        token = data.token
                        console.log(token)
                        console.log("mystore: "+ mystore)
                        mystore.commit('set_token',"Token "+ token)
                        console.log("token: " + mystore.state.token)
                        myrouter.push({path :'/dashboard' })
                    },
                    error: function() {
                        console.log('Login Faild!')
                    }
                })

                
            },

            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        this.sendPost()                    
                    } else {
                        this.$Message.error('2 Login Faild!')
                    }
                })
            }
        }
    }
</script>

<style type="text/css" lang="less">
	.p-color {
		color: red;
	}

</style>
