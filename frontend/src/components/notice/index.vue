
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
				// dialog_status 用于复用 el-dialog
				dialog_status: "addNotice",
				all_notice : [],
				notice_count : 0
			}
		},
		methods:{
			// 初始化notice_list
			set_notice_list(data) {
				this.notice_list = data
			},
			set_all_notice(data){
				this.all_notice = data.results
				this.notice_count = data.count
			},
			//日期格式化
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
			// 状态转换
			notice_code(code){
				if (code === 0){
					return "未开始"
				}
				else if (code === 1) {
					return "已完成"
				}
				else if (code === 2) {
					return "进行中"
				}
				else if( code === 3) {
					return "拒  绝"
				}
				else {
					return "未知状态："+ code
				}
			},
			// 控制el-tag 标签的类型
			notice_type(code){
				if (code === 0){
					return "warning"
				}
				else if (code === 1) {
					return "success"
				}
				else if (code === 2) {
					return ""
				}
				else if( code === 3) {
					return "danger"
				}
				else {
					return ""
				}
			},
			// 刷新页面数据
			refresh_data(){
				Notice.get_notice(this.currentPage,this.token, this.set_notice_list)
				Notice.all_notice(this.currentPage,this.token, this.set_all_notice)
			},
			// 处理model的提交操作, 配合dialog_status一起使用
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
					console.log(JSON.stringify(this.the_form) )
					Notice.edit_notice(this.the_form,this.token,function(data){
						alert("更新成功")
						this.refresh_data()
					}.bind(this))
				}
				this.dialogFormVisible = false
			},
			// 添加按钮响应事件
			add_notice(){
				this.dialog_status = "addNotice"
				this.the_form = {"datetime": "" ,"notice_item":"","status": 0, "schedule": "1.20"}
				this.dialogFormVisible = true
			},
			// 编辑按钮响应事件
			edit_notice(notice){
				this.the_form = JSON.parse(JSON.stringify(notice) )
				this.dialog_status = "editNotice"
				this.dialogFormVisible = true
			},
			handlePageChange() {
				Notice.all_notice(this.currentPage,this.token, this.set_all_notice)
			}
		},
		created(){
			Notice.get_notice(this.currentPage,this.token, this.set_notice_list)
			Notice.all_notice(this.currentPage,this.token, this.set_all_notice)
			setInterval(()=>{//钩子函数，在实例创建的时候运行定时器，我们只需要动态刷新当前的日期对象即可
				this.current_date = new Date();
				//console.log(this.current_date)
			},10000)
		},
		computed: {
			my_list : function(){
				console.log(this.notice_list)
				return this.notice_list
			},
			all_list : function() {
				return this.all_notice
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
		<div id="notice_carousel"> 
			<div v-if="my_list.length == 0">
				<p>暂无任务</p>	
			</div>
			<template v-else>
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
					    <p>任务状态：<el-tag size="small" :type="notice_type(item.status)">{{notice_code(item.status)}}
					    	</el-tag>  </p>
					  </div>
					</el-card>
			    </el-carousel-item>
			  </el-carousel>
			</template>
		</div>
		<div id="notice_table">
			<el-table
				:data="all_list"
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
				  label="计划内容"
				  width="220">
				  <template slot-scope="scope">
				    <i class="el-icon-time"></i>
				    <span style="margin-left: 10px">{{ scope.row.notice_item }}</span>
				  </template>
				</el-table-column>
				<el-table-column
				  label="计划开始时间"
				  width="180">
				  <template slot-scope="scope">
				  	<i class="el-icon-time"></i>
				    <span style="margin-left: 10px">{{ formatDate(scope.row.datetime)}}</span>
				  </template>
				</el-table-column>
				<el-table-column
				  label="计划时长"
				  width="120">
				  <template slot-scope="scope">
				    <span style="margin-left: 10px">{{scope.row.schedule}} h</span>
				  </template>
				</el-table-column>
				<el-table-column
				  label="计划状态"
				  width="180">
				  <template slot-scope="scope">
				    <el-tag size="small" :type="notice_type(scope.row.status)">{{notice_code(scope.row.status)}}</el-tag>
				  </template>
				</el-table-column>
				<el-table-column label="操作">
				  <template slot-scope="scope">
				    <el-button
				      size="mini" icon="el-icon-edit"
				      @click="edit_notice(scope.row)">编辑</el-button>
				  </template>
				</el-table-column>
			</el-table>
			<div class="block" id = "notice_pagination">
				<el-pagination
				  @current-change="handlePageChange"
				  :current-page.sync="currentPage"
				  :page-size="10"
				  layout="total, prev, pager, next"
				  :total="notice_count">
				</el-pagination>
			</div>
		</div>

		<el-dialog title="新增Notice" :visible.sync="dialogFormVisible">
		  <el-form label-position="left" :model="the_form">
		    <el-form-item label="计划时间:" >
		    	<el-date-picker
			      v-model="the_form.datetime"
			      type="datetime"
			      placeholder="选择日期时间">
			    </el-date-picker>
		    </el-form-item>
		    <el-form-item label="计划内容:" :disabled="dialog_status == 'editNotice' ? false : true ">
		    	<el-input v-model="the_form.notice_item"></el-input>
		    </el-form-item>
		    <el-form-item label="计划时长:">
		    	<el-input-number v-model="the_form.schedule" :precision="2" :step="0.2" :max="10"></el-input-number>
		    </el-form-item>
		    <el-form-item v-if="dialog_status === 'editNotice' " label="计划状态:">
		    	<el-radio-group v-model="the_form.status">
					<el-radio :label="0"><el-tag size="small" :type="notice_type(0)">{{notice_code(0)}}</el-tag> </el-radio>
					<el-radio :label="1"><el-tag size="small" :type="notice_type(1)">{{notice_code(1)}}</el-tag></el-radio>
					<el-radio :label="2"><el-tag size="small" :type="notice_type(2)">{{notice_code(2)}}</el-tag></el-radio>
					<el-radio :label="3"><el-tag size="small" :type="notice_type(3)">{{notice_code(3)}}</el-tag></el-radio>
				</el-radio-group>
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