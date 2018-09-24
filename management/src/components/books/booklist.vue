<template>
<div > 
	<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
          @click="form_new_book">添加书籍</el-button>
    <el-button style="float: right;" type="success" size="mini" @click="refresh_data" >刷新</el-button> 
	<div id = "booklist">
		<br>
		<el-card v-for="book in books" :key="book.id + new Date()" shadow="hover" >
		  <div slot="header" class="clearfix" @dblclick="view_detail(book)" >
		    <el-row :gutter="20"  >	
		    	<h3 style="float: left;" > {{book.name}} </h3>
		    <el-button  style="float: right; margin-left:10px  " type="primary" icon="el-icon-edit" circle 
		    	@click="form_edit_book(book)" ></el-button>
		    <el-button style="float: right; margin-left:10px "  type="danger" icon="el-icon-delete" circle  
		    	@click="form_remove_book(book)" ></el-button>
		    </el-row>	
		  </div>
		  <p><el-tag size="medium" type="success">作者：</el-tag> {{book.author}}</p>
		  <p><el-tag size="medium">书籍类别：</el-tag> {{book.book_style}}</p>
		  <p><el-tag size="medium">内容简介：</el-tag> {{book.introduction}}</p>
		</el-card>
	</div>
	<el-dialog :title="dialogStatus" :visible.sync="dialogFormVisible">
	  <el-form label-position="left" label-width="80px" :model="currentBook">
	    <el-form-item label="书名:" >
	    	<el-input v-model="currentBook.name"></el-input>
	    </el-form-item>
	    <el-form-item label="作者:">
	    	<el-input v-model="currentBook.author"></el-input>
	    </el-form-item>
	    <el-form-item label="书籍类别:">
	    	<el-input v-model="currentBook.book_style"></el-input>
	    </el-form-item>
	    <el-form-item label="内容简介:">
	    	<el-input v-model="currentBook.introduction"></el-input>
	    </el-form-item>
	  </el-form>
	  <div slot="footer" class="dialog-footer">
	    <el-button @click="dialogFormVisible = false">取 消</el-button>
	    <el-button type="primary" @click="handle_submmit">提 交</el-button>
	  </div>
	</el-dialog>
</div>
</template>

<script type="text/javascript">
import {Books} from '@/utils/ajaxFunctions'
export default {
	name:"books",
	data() {
		return {
			books :[],
			dialogFormVisible: false,
			currentBook : {"name":"","author":"","book_style":""},
			count : 0 ,
			currentPage: 1,
			token: this.$store.state.token,
			dialogStatus: "editBook"
		}		 
	},
	methods: {
		set_list(data) {
			this.books = data.results
			this.count = data.count
		},
		refresh_data() {
			Books.get_book_list(this.currentPage,this.token,this.set_list)
		},
		form_edit_book(book) {
			console.log("Edit the Book")
			this.currentBook = book
			this.dialogStatus =  "editBook"
			this.dialogFormVisible = true
		},
		form_remove_book(book) {
			console.log("Edit the Book")
			this.currentBook = book
			this.$confirm('确定要删除本书吗？', '提示', {
	          confirmButtonText: '确定',
	          cancelButtonText: '取消',
	          type: 'warning'
	        }).then(() => {
	        	this.axios_remove_book()
	          	this.$message({
	            type: 'success',
	            message: '删除成功!'
	          });
	        }).catch(() => {
	          this.$message({
	            type: 'info',
	            message: '已取消删除'
	          });          
	        });
			console.log("Remove the Book")
		},
		form_new_book() {
			console.log("New Book")
			this.dialogStatus =  "addBook"
			this.currentBook = {"name":"","author":"","book_style":"","introduction":""}
			this.dialogFormVisible = true
		},
		handle_submmit() {
			console.log("Submmit Edit")
			if (this.dialogStatus ==  "addBook" ) {
				this.axios_add_book()
			}
			else if (this.dialogStatus ==  "editBook") {
				this.axios_edit_book()
			}
			this.refresh_data()
			this.dialogFormVisible = false
		},
		axios_add_book(){
			Books.new_book(this.currentBook,this.token,this.set_list)
		},
		axios_edit_book(){
			Books.edit_book(this.currentBook,this.token,this.set_list)
		},
		axios_remove_book() {
			Books.delete_book(this.currentBook,this.token,this.set_list)
		},
		view_detail(book) {
			this.$router.push("/books/bookcontent/"+book.id)
		}
	},
	created: function(){
		Books.get_book_list(this.currentPage,this.token,this.set_list)
	}
}
</script>