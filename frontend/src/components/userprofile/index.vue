
<script type="text/javascript">
	import $ from 'jquery'
	// import showuser from './showuser'
	import {mapState} from 'vuex'
	import login from '../login'
	export default {
		name: 'home',
		data() {
			return  {
				users1 : [],
				columns1: [
					{
						title: "id",
						key : "id"
					},
					{
						title: "user_name",
						key : "user_name"
					},
					{
						title: "device_no",
						key : "device_no"
					}],
				formLeft: {
                    input1: '',
                    input2: '',
                    input3: ''
                },
                modal6: false,
                edituser: false,
                loading: true,
                currentuser: {}
			}
		},
		methods: {
			get_device(callback) {
				var mytoken = this.$store.state.token
				var myusers = $.ajax({
					url:"/rocky/device/",
					type:"GET",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					success: function(data){
						console.log(data)
						// callback =  data
					},
					error: function(err){
						console.log(err)
						alert(err)
					}
				}).done(callback)
			},
			creat_device(user,callback){
				var mytoken = this.$store.state.token
				var myusers = $.ajax({
					url:"/rocky/device/",
					type:"POST",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					data: JSON.stringify(user),
					success: function(data){
						console.log(data)
						// callback =  data
					},
					error: function(err){
						console.log(err)
						alert(err)
					}
				}).done(callback)
			},
			setusers(data) {
				console.log(data)
				this.users1 = data
			},
			asyncOK () {
				var _this = this
				var currentuser = _this.currentuser
				currentuser.project_id = 1
				currentuser.channel_id = 1
				console.log(JSON.stringify(currentuser) )
				_this.creat_device(currentuser,function(data){
					alert(data)
					_this.get_device(_this.setusers)
					setTimeout(() => {
                    	_this.modal6 = false;
                	}, 2000);
				}).bind                
            },
            select_current_user(currentRow,oldCurrentRow){
            	console.log(currentRow,oldCurrentRow)
            	this.currentuser = currentRow
            },
            row_dblclick(currentRow,index){
            	this.currentuser = currentRow
            	this.modal6 = true
            },
            creat_user() {
            	this.currentuser = {id:'', device_no: '', project_id: 1, user_name:'' , channel_id: 1}
            	this.modal6 = true
            },
            delete_user() {
            	var mytoken = this.$store.state.token
            	var user = this.currentuser
            	var _this =  this 
            	$.ajax({
					url:"/rocky/device/"+user.id+"/",
					type:"DELETE",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					error: function(err){
						console.log(err)
						alert(err,"删除失败")
					}
            	}).done(function(){
            		alert("删除成功")
            		_this.get_device(_this.setusers)
            	})
            },
            edit_user() {
            	var mytoken = this.$store.state.token
            	var user = this.currentuser
            	var _this =  this 
            	$.ajax({
					url:"/rocky/device/"+user.id+"/",
					type:"PUT",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					data: JSON.stringify(user),
					error: function(err){
						console.log(err)
						alert(err,"修改失败")
					}
            	}).done(function(){
            		alert("修改成功")
            		_this.edituser = false
            		_this.get_device(_this.setusers)
            	})
            }
		},
		created: function(){
			this.get_device(this.setusers)
		},
		computed:{
			data1: function() {
				return this.users1
			}
		},
		watch: {
			users1: function() {
				console.log(this.users1)
			}
		}			

	}
</script>


<template>
	<div>
		<h1>Hello Rocky</h1>
		<P>这是主页</P>
		<button v-on:click="get_device()">Submmit!</button>
		<div v-if="users1">
			{{users1}}
			<br/>
		<Button type="primary" @click="edituser = true">编辑用户</Button>
		<Button type="primary" @click="creat_user">创建用户</Button>
		<Button type="primary" @click="delete_user">删除用户</Button>
		<Table highlight-row ref="currentRowTable" @on-current-change="select_current_user" 
			@on-row-dblclick="row_dblclick" :columns="columns1" :data="data1"></Table>
		<!-- <showuser  ></showuser> -->
		
	    <Modal
	        v-model="modal6"
	        title="Title"
	        :loading="loading"
	        @on-ok="asyncOK">
	        <p>After you click ok, the dialog box will close in 2 seconds.</p>
		    <template>
				<Form :model="formLeft" label-position="left" :label-width="100">
			        <FormItem label="device_no">
			            <Input v-model="currentuser.device_no"></Input>
			        </FormItem>
			        <FormItem label="user_name">
			            <Input v-model="currentuser.user_name"></Input>
			        </FormItem>
			    </Form>
			</template>
	    </Modal>

	    <Modal
	        v-model="edituser"
	        title="Title"
	        :loading="loading"
	        @on-ok="edit_user">
	        <p>After you click ok, the dialog box will close in 2 seconds.</p>
		    <template>
				<Form :model="formLeft" label-position="left" :label-width="100">
			        <FormItem label="device_no">
			            <Input v-model="currentuser.device_no"></Input>
			        </FormItem>
			        <FormItem label="user_name">
			            <Input v-model="currentuser.user_name"></Input>
			        </FormItem>
			    </Form>
			</template>
	    </Modal>
		
		</div>
	</div>
</template>