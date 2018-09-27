<template>
  <div id="chapterdtail">
    <el-row :gutter="20">
      <el-col :span="14">
        <el-card class="box-card" :key="currentChapter.updated_at">
          <div slot="header" class="clearfix" @dblclick="edit_chaptert(currentChapter)">
            <h3>{{currentChapter.chapter}}</h3>
            <router-link :to="'/books/bookcontent/'+currentChapter.book_id" style="float: right; padding: 3px 0">章节目录</router-link>
          </div>
          <div id="chaptercontent" v-html="currentChapter.content"></div>
        </el-card>
      </el-col>
      <el-col :span="10">
        <div class="block" style="position:fixed; overflow: hidden;" id="comments">
          <div id="input_comments" >
          	  <editorelem style="background-color:#FFF5EE"
                :key="editorelem_key"  :catchData="catchCommentData" :editorindex="1000">
              </editorelem>
            <!-- <el-input type="textarea" :rows="3" placeholder="请输入笔记内容" v-model="newcommet"> </el-input> -->
            <el-button type="success" plain icon="el-icon-circle-plus-outline" @click="new_comment">提交</el-button>
          </div>
          <div class="demo_line_01"><b><span>随笔：</span></b> </div> 
          <div id="comment_container" style="position: relative;overflow: hidden; height: 600px" >
        <div id="chaptercomments" style="height: 500px;overflow-y: auto; overflow-x: hidden;">
          <el-card v-for="comment in comments" :key="comment.id" :body-style="{ padding: '10px' }" >
            <div id="chaptercontent" class="comment" v-html="comment.comments"></div>
            <HR style="border:1 dashed " width="100%" color=#ddd  SIZE=1 />
            <div  class="comment-head "  >
              <span >{{fromat_date(comment.created_at)}}</span>
              <el-button style="float: right; padding: 3px 0" type="text" @click="delete_comment(comment)" ><i class="el-icon-delete"></i></el-button>
            </div>
          </el-card>
          <el-pagination background v-if="comment_count != 0" @current-change="axios_get_comments" :current-page.sync="comments_page" 
            :page-size="10" layout="prev, pager, next" :total="comment_count">
          </el-pagination>
        </div>
        </div>
        </div>
      </el-col>
    </el-row>
    <!-- 章节编辑输入框 -->
    <el-dialog title="添加章节" :visible.sync="dialogFormVisible">
      <el-form label-position="left" label-width="80px" :model="modify_chapter">
        <el-form-item label="章节名称:">
          <el-input v-model="modify_chapter.chapter" disable></el-input>
        </el-form-item>
        <!-- <el-form-item label="章节名称:">
          <el-input v-model="currentChapter.content"></el-input>
        </el-form-item> -->
        <el-form-item label="正文:">
          <editorelem :key="modify_chapter.editor" :catchData="catchData" :content="currentChapter.content"></editorelem>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click.native="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click.native="handle_submmit">提 交</el-button>
      </div>
    </el-dialog>
    <footer >2017-2018 &copy; Rocky   </footer>
  </div>
  
</template>
<script type="text/javascript">
import { Books } from "@/utils/ajaxFunctions";
import { tools } from "@/utils/tools";
import editorelem from "@/components/rocky/editor";
export default {
  name: "chapter",
  data() {
    return {
      currentChapter: {},
      chapterId: this.$route.params.chapter_id,
      token: this.$store.state.token,
      comments_page: 1,
      comments: {},
      comment_count: 0,
      current_comment: {
        chapter_id: this.$route.params.chapter_id,
        comments: ""
      },
      dialogFormVisible: false,
      newcommet: "",
      modify_chapter: { editor: new Date().getTime() },
      editorelem_key: new Date().getTime()
    };
  },
  methods: {
    set_chapter_data(data) {
      this.currentChapter = data;
    },
    set_comment_data(data) {
      this.comments = data.results;
      this.comment_count = data.count;
    },
    axios_get_chapter() {
      Books.get_chapter_detail(
        this.chapterId,
        this.token,
        this.set_chapter_data
      );
    },
    axios_get_comments() {
      Books.get_chapter_comment(
        this.chapterId,
        this.comments_page,
        this.token,
        this.set_comment_data
      );
    },
    refresh_data() {
      this.axios_get_chapter();
      this.axios_get_comments();
    },
    fromat_date(time) {
      return tools.formatDate(time);
    },
    new_comment() {
      this.current_comment = {
        chapter_id: this.$route.params.chapter_id,
        comments: this.newcommet
      };
      if (this.newcommet == "") {
        this.$message({
          message: "评论内容不能为空！！！",
          type: "warning"
        });
      } else {
        Books.add_comment(this.current_comment, this.token, data => {
          console.log(data);
          this.refresh_data();
          this.newcommet = "";
          this.editorelem_key = new Date().getTime();
        });
      }
    },
    catchData(val) {
      this.modify_chapter.content = val;
    },
    catchCommentData(val) {
      this.newcommet = val;
    },
    edit_chaptert(chapter) {
      this.dialogFormVisible = true;
      this.modify_chapter = { editor: new Date().getTime() };
      Object.assign(this.modify_chapter, chapter);

      this.modify_chapter.updated_at = new Date();
      console.log(this.modify_chapter);
    },
    handle_submmit() {
      console.log(this.modify_chapter);
      this.dialogFormVisible = false;
      Books.edit_book_chapter(this.modify_chapter, this.token, data => {
        this.refresh_data();
      });
    },
    delete_comment(comment) {
      Books.remove_comment(comment, this.token, data => {
        this.refresh_data();
      });
    }
  },
  created: function() {
    Books.get_chapter_detail(this.chapterId, this.token, this.set_chapter_data);
    Books.get_chapter_comment(
      this.chapterId,
      this.comments_page,
      this.token,
      this.set_comment_data
    );
  },
  components: {
    editorelem
  }
};
</script>
<style>
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
  clear: both;
}

.box-card {
  min-height: 800px;
  width: 100%;
}

#chaptercomments {
  padding: 10px;
}
footer {
  text-align: center;
  padding: 30px;
}
/* 分隔线  */
.demo_line_01 {
  position: relative;
  padding: 0 10px 0;
  margin: 20px 0;
  line-height: 1px;
  border-left: 20px solid rgb(197, 196, 196);
  border-right: 400px solid #ddd;
  text-align: center;
}

.comment {
  padding: 5px;
  /* background-color: ivory; */
}
.comment-head {
  margin-top: 15px;
  /* border-top: 1px solid #ebeef5; */
  text-align: left;
}
</style>
