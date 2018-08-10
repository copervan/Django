
<script type="text/javascript">
	import {Notice} from '../../utils/ajaxFunctions'

	export default {
		name: 'notice',
		data() {
			return {
				notice_list : [],
				dialogFormVisible : false,
				the_form: {"datetime": "" ,"notice_item":"","status":0},
				currentPage: 1,
				token: this.$store.state.token,
				current_date : Date(),
				dialog_status: "addNotice"
			}
		},
		methods:{
			formatDate(time){
			    var date = new Date(time);

			    var year = date.getFullYear(),
			        month = date.getMonth()+1,//月份是从0开始的
			        day = date.getDate(),
			        hour = date.getHours(),
			        min = date.getMinutes(),
			        sec = date.getSeconds();
			    var newTime = year + '-' +
			                (month < 10? '0' + month : month) + '-' +
			                (day < 10? '0' + day : day) + ' ' +
			                (hour < 10? '0' + hour : hour) + ':' +
			                (min < 10? '0' + min : min) + ':' +
			                (sec < 10? '0' + sec : sec);

			    return newTime;         
			},
			set_notice_list(data) {
				this.notice_list = data
			},
			formatDate(time){
			    var date = new Date(time);

			    var year = date.getFullYear(),
			        month = date.getMonth()+1,//月份是从0开始的
			        day = date.getDate(),
			        hour = date.getHours(),
			        min = date.getMinutes(),
			        sec = date.getSeconds();
			    var newTime = year + '-' +
			                (month < 10? '0' + month : month) + '-' +
			                (day < 10? '0' + day : day) + ' ' +
			                (hour < 10? '0' + hour : hour) + ':' +
			                (min < 10? '0' + min : min) ;
			                //+ ':' + (sec < 10? '0' + sec : sec);

			    return newTime;         
			},
			notice_code(code){
				if (code == 0){
					return "未完成"
				}
				else if (code == 1) {
					return "已完成"
				}
				else {
					return "未知状态："+ code
				}
			},
			refresh_data(){
				Notice.get_notice(this.currentPage,this.token, this.set_notice_list)
			},
			handle_submmit() {
				if (this.dialog_status == "addNotice"){
					// 添加Notice
					Notice.create_notice(this.the_form,this.token, function(data){
						alert("创建成功")
						this.refresh_data()
					}.bind(this))
				}
				else if (this.dialog_status == "editNotice"){
					// 编辑Notice
				}
				this.dialogFormVisible = false
			},
			add_notice(){
				this.dialog_status = "addNotice"
				this.the_form = {"datetime": "" ,"notice_item":"","status": 0, "schedule": "1.20"}
				this.dialogFormVisible = true
			},
			edit_notice(notice){
				this.the_form = notice
				this.dialog_status = "editNotice"
				this.dialogFormVisible = true
			}
		},
		created(){
			Notice.get_notice(this.currentPage,this.token, this.set_notice_list)
			setInterval(()=>{//钩子函数，在实例创建的时候运行定时器，我们只需要动态刷新当前的日期对象即可
				this.current_date = new Date();
				//console.log(this.current_date)
			},10000)
		},
		computed: {
			my_list : function(){
				console.log(this.notice_list)
				return this.notice_list
			}
		}
	}
</script>

<template>
	<div padding="20px">
		<br/>
		<h1>当前时间: {{formatDate(current_date)}}</h1><br/>
		<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
		 @click="add_notice">新增Notice</el-button>
		<el-button style="float: right;" type="success" size="mini" @click="refresh_data" >刷新</el-button>
		<!-- todolist 轮播图-->
		<div> 
			<template>
			  <el-carousel :interval="4000" type="card" height="300px">
			    <el-carousel-item v-for="item in my_list" :key="item">
			      	<el-card class="box-card">
					  <div slot="header" class="clearfix">
					    <h2><span>计划内容：{{item.notice_item}}</span></h2>
					    <el-button style="float: right; padding: 3px 0" type="success" @click="edit_notice(item)">操作按钮</el-button>
					  </div>
					  <div class="text item" >
					    <p>计划开始时间：{{formatDate(item.datetime)}}</p>
					    <p>计划时长：{{item.schedule}} h</p>
					    <p>任务状态：<el-tag v-if="" size="small" :type="item.status === 0 ? 'danger' : 'success' ">{{notice_code(item.status)}}</el-tag>
					    	</el-tag>
					    </p>
					  </div>
					</el-card>
			    </el-carousel-item>
			  </el-carousel>
			</template>
		</div>

		<el-dialog title="新增Notice" :visible.sync="dialogFormVisible">
		  <el-form label-position="top" :model="the_form">
		    <el-form-item label="计划时间" >
		    	<el-date-picker
			      v-model="the_form.datetime"
			      type="datetime"
			      placeholder="选择日期时间">
			    </el-date-picker>
		    </el-form-item>
		    <el-form-item label="计划内容">
		    	<el-input v-model="the_form.notice_item"></el-input>
		    </el-form-item>
		    <el-form-item label="计划时长">
		    	<el-input v-model="the_form.schedule"></el-input>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="dialogFormVisible = false">取 消</el-button>
		    <el-button type="primary" @click="handle_submmit">确 定</el-button>
		  </div>
		</el-dialog>
	</div>
</template>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
</style>