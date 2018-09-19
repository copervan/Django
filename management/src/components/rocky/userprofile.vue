
<script type="text/javascript">
	import {Users} from '@/utils/ajaxFunctions'
	import {mapState} from 'vuex'
	import login from './login'
	export default {
		name: 'home',
		data() {
			return  {
				users1 : [],
				user_count: 0,
				currentPage: 1,
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
                currentuser: {},
                token: this.$store.state.token
			}
		},
		methods: {
			setusers(data) {
				// console.log(data)
				this.users1 = data.results
				this.user_count = data.count
			},
			asyncOK () {
				var _this = this
				this.currentuser.project_id = 1
				this.currentuser.channel_id = 1
				// console.log(JSON.stringify(this.currentuser),this.token)
				Users.creat_device(_this.currentuser,_this.token, function(data){
					// alert(data)
					Users.get_device(_this.currentPage, _this.token, _this.setusers)
					setTimeout(() => {
                    	_this.modal6 = false;
                	}, 500);
				})          
            },
            creat_user() {
            	this.currentuser = {id:'', device_no: '', project_id: 1, user_name:'' , channel_id: 1}
            	this.modal6 = true
            },
            submmit_edit() {
            	var _this = this
            	// console.log(_this.token)
            	Users.edit_user(_this.currentuser,_this.token,function(){
            		Users.get_device(_this.currentPage, _this.token, _this.setusers)
            		_this.edituser = false;
            	})
            },
            delete_user() {
            	var _this = this
            	// console.log(_this.token)
            	Users.delete_user(_this.currentuser,_this.token,function(){
            		Users.get_device(_this.currentPage,_this.token, _this.setusers)
            	})
            },
            handleEdit(index, row) {
            	console.log(row)
            	this.currentuser =  JSON.parse(JSON.stringify(row))
            	// console.log(this.currentuser)
            	this.edituser = true
		    },
			handleDelete(index, row) {
				console.log(row)
				this.currentuser = JSON.parse(JSON.stringify(row))
				// console.log(this.currentuser)
				this.delete_user()
			},
			handleCurrentChange() {
				var _this = this
				Users.get_device(_this.currentPage, _this.token, _this.setusers)
			},
			refresh_data(){
				Users.get_device(this.currentPage,this.token, this.setusers)
			}
		},
		created: function(){
			Users.get_device(this.currentPage,this.token, this.setusers)
		},
		computed:{
			data1: function() {
				// console.log(this.users1)
				return this.users1
			}
		}		
	}
</script>


<template>
	<div>
		<h1>Hello Rocky</h1>
		<P>这是主页</P><br/>
		<div v-if="users1">
		<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
          @click="creat_user">创建用户</el-button> 
        <el-button style="float: right;" type="success" size="mini" @click="refresh_data" >刷新</el-button>

<!-- 			<Button type="primary" @click="creat_user">创建用户</Button> -->
			<!-- <Table highlight-row ref="currentRowTable" @on-current-change="select_current_user"  -->
				<!-- @on-row-dblclick="row_dblclick" :columns="columns1" :data="data1"></Table> -->
		<!-- 用户列表模块 -->
		<template>
			<div>
				<br/>
			<el-table
			:data="data1"
			style="width: 100%">
			<el-table-column
			  label="ID"
			  width="180">
			  <template slot-scope="scope">
			    <i class="el-icon-time"></i>
			    <span style="margin-left: 10px">{{ scope.row.id }}</span>
			  </template>
			</el-table-column>
			<el-table-column
			  label="User_Name"
			  width="180">
			  <template slot-scope="scope">
			    <i class="el-icon-time"></i>
			    <span style="margin-left: 10px">{{ scope.row.user_name }}</span>
			  </template>
			</el-table-column>
			<el-table-column
			  label="Device_No"
			  width="180">
			  <template slot-scope="scope">
			    <el-popover trigger="hover" placement="top">
			      <p>project_id: {{ scope.row.project_id }}</p>
			      <p>channel_id: {{ scope.row.channel_id }}</p>
			      <div slot="reference" class="name-wrapper">
			        <el-tag size="medium">{{ scope.row.device_no }}</el-tag>
			      </div>
			    </el-popover>
			  </template>
			</el-table-column>
			<el-table-column label="操作">
			  <template slot-scope="scope">
			    <el-button
			      size="mini" icon="el-icon-edit"
			      @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
			    <el-button
			      size="mini"
			      type="danger" icon="el-icon-delete"
			      @click="handleDelete(scope.$index, scope.row)">删除</el-button>
			  </template>
			</el-table-column>
			</el-table>
			<div class="block">
			<el-pagination
			  @current-change="handleCurrentChange"
			  :current-page.sync="currentPage"
			  :page-size="10"
			  layout="total, prev, pager, next"
			  :total="user_count">
			</el-pagination>
			</div>
			</div>
		</template>


		</div>
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
	        @on-ok="submmit_edit">
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
</template>