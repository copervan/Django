

<script type="text/javascript">
	export default {
		name: 'notice',
		data() {
			return {
				notice_list : [],
				dialogFormVisible : false,
				the_form: {"datetime": "" ,"notice_item":""}
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
			}

		},
		computed: {
			current_date: function() {
				return this.formatDate(Date())
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