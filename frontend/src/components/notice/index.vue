
<script type="text/javascript">
	import {Notice} from '../../utils/ajaxFunctions'

	export default {
		name: 'notice',
		data() {
			return {
				notice_list : [],
				dialogFormVisible : false,
				the_form: {"datetime": "" ,"notice_item":""},
				currentPage: 1,
				token: this.$store.state.token
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
				this.notice_list = data.results
			}

		},
		created: function() {
			// console.log('this is the create' )
			Notice.get_notice(this.currentPage,this.token, this.set_notice_list)
		},
		computed: {
			current_date: function() {
				return this.formatDate(Date())
			},
			my_list : function(){
				console.log(this.notice_list)
				return this.notice_list
			}
		}
	}
</script>

<template>
	<div padding="20px">
		<h1>当前时间: {{current_date}}</h1><br/>
		<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
		 @click="dialogFormVisible = true">新增Notice</el-button>
		<!-- todolist -->
		<div> 
			<template>
			  <el-carousel :interval="4000" type="card" height="200px">
			    <el-carousel-item v-for="item in my_list" :key="item">
			      <h3>{{ item.notice_item }}</h3>
			    </el-carousel-item>
			  </el-carousel>
			</template>
		</div>

		<el-dialog title="新增Notice" :visible.sync="dialogFormVisible">
		  <el-form :model="the_form">
		    <el-form-item label="计划时间" >
		    	<el-date-picker
			      v-model="the_form.datetime"
			      type="datetime"
			      placeholder="选择日期时间">
			    </el-date-picker>
		    </el-form-item>
		    <el-form-item label="计划内容">
		      <el-select v-model="the_form.notice_item" placeholder="请选择活动区域">
		        <el-option label="区域一" value="shanghai"></el-option>
		        <el-option label="区域二" value="beijing"></el-option>
		      </el-select>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="dialogFormVisible = false">取 消</el-button>
		    <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
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
</style>