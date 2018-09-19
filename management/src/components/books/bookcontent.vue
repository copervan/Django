<template>
	<div id = "booklist">
		<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
          @click="new_diary">Create The Diary</el-button>
        <el-button style="float: right;" type="success" size="mini" @click="refresh_data" >刷新</el-button>
        
		<el-card v-for="book in books" :key="book.id" :offset="index > 0 ? 2 : 0">
		  <div slot="header" class="clearfix">
		    <h4>{{book.name}}</h4>
		    <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
		  </div>
		  <div v-for="o in 4" :key="o" class="text item">
		    {{'列表内容 ' + o }}
		  </div>
		</el-card>
	</div>
</template>

<script type="text/javascript">
import {Books} from '@/utils/ajaxFunctions'
export default {
	name:"books",
	data() {
		return {
			bookContents :[],
			count : 0 ,
			currentPage: 1,
			token: this.$store.state.token
		}		
	},
	methods: {
		set_list(data) {
			this.books = data.results
			this.count = data.count
		}
	},
	created: function(){
		Books.get_book_list(this.currentPage,this.token,this.set_list)
	}
}
</script>