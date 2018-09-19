<template>
<div > 
	<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
          @click="new_diary">添加书籍</el-button>
    <el-button style="float: right;" type="success" size="mini" @click="refresh_data" >刷新</el-button> 
	<div id = "booklist">
		<br>
		<el-card v-for="book in books" :key="book.id + new Date()">
		  <div slot="header" class="clearfix">
		    <h4>{{book.name}}</h4>
		    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
		  </div>
		  <div v-for="o in 4" :key="o" class="text item">
		    {{'列表内容 ' + o }}
		  </div>
		</el-card>
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

<script type="text/javascript">
import {Books} from '../../utils/ajaxFunctions'
export default {
	name:"books",
	data() {
		return {
			books :[],
			dialogFormVisible: false,
			currentBook : {},
			count : 0 ,
			currentPage: 1,
			token: this.$store.state.token
		}		
	},
	methods: {
		set_list(data) {
			this.books = data.results
			this.count = data.count
		},
		refresh_data() {
			Books.get_book_list(this.currentPage,this.token,this.set_list)
		}
	},
	created: function(){
		Books.get_book_list(this.currentPage,this.token,this.set_list)
	}
}
</script>