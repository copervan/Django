<template>
	<div id = "bookcontent">
		<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
          @click="new_chapter">添加章节</el-button>
        <el-button style="float: right;" type="success" size="mini" @click="refresh_data" >刷新</el-button>

		<div id = "book">
			<br>
			<el-card :key="bookContents.id + new Date()" shadow="hover" >
			  <div slot="header" class="clearfix" >
			    <h3 > {{bookContents.name}} </h3>
			  </div>
			  <p><el-tag size="medium" type="success">作者：</el-tag> {{bookContents.author}}</p>
			  <p><el-tag size="medium">书籍类别：</el-tag> {{bookContents.book_style}}</p>
			  <p><el-tag size="medium">内容简介：</el-tag> {{bookContents.introduction}}</p>
			</el-card>
		</div> <br>
		<p>章节列表：</p>
		<div style="margin-left: 50px">
      <ol>
      <div class="chapter_list"  v-for="(chapter,index) in bookContents.book_content" >
        <router-link :to="'/books/chapter/'+chapter.id">	<li> {{chapter.chapter}}</li></router-link> 
        <!-- <router-link :to="routerTo(chapter,index)">	<li> {{chapter.chapter}}</li></router-link> -->
      </div>
      </ol>
      <footer style="height: 50px"></footer>
    </div>
    <router-view></router-view>

    <el-dialog title="添加章节" :visible.sync="dialogFormVisible">
	  <el-form label-position="left" label-width="80px" :model="newChapter">
	    <el-form-item label="书名:" >
	    	<el-input v-model="bookContents.name" ></el-input>
	    </el-form-item>
	    <el-form-item label="章节名称:">
	    	<el-input v-model="newChapter.chapter" ></el-input>
	    </el-form-item>
	    <el-form-item label="正文:">
	    	<editorelem :key="newChapter.editor" :catchData="catchData"  ></editorelem>
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
import { Books } from "@/utils/ajaxFunctions";
import editorelem from "@/components/rocky/editor";
export default {
  name: "bookcontents",
  data() {
    return {
      book_id: this.$route.params.book_id,
      bookContents: {},
      token: this.$store.state.token,
      dialogFormVisible: false,
      newChapter: {
        book_id: this.book_id,
        chapter: "",
        content: "",
        editor: new Date().getTime()
      }
    };
  },
  methods: {
    set_list(data) {
      this.bookContents = data;
      console.log(JSON.stringify(this.bookContents));
    },
    refresh_data() {
      Books.get_book_content(this.book_id, this.token, this.set_list);
    },
    new_chapter() {
      this.newChapter = {
        book_id: this.bookContents.id,
        chapter: "",
        content: "",
        editor: new Date().getTime()
      };
      this.dialogFormVisible = true;
    },
    handle_submmit() {
      Books.add_book_chapter(this.newChapter, this.token, data => {
        this.refresh_data();
      });
      this.dialogFormVisible = false;
    },
    catchData(value) {
      this.newChapter.content = value; //在这里接受子组件传过来的参数，赋值给data里的参数
    },
  },
  created: function() {
    Books.get_book_content(this.book_id, this.token, this.set_list);
  },
  components: {
    editorelem
  }
};
</script>

<style>
.chapter_list {
  width: 200px;
	margin-top: 15px;
	float: left;
	list-style-type: square type decimal;
}
</style>
