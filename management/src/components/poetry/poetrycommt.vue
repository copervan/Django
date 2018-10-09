<template>
    <div id="poetry_detail">
        <el-row :gutter="20" >
            <el-col :span="14">
        <el-card class="box-card" :key="currentPoetry.id">
            <div slot="header" class="clearfix" >
                <span>{{currentPoetry.title}}</span>
            </div>
            <p><el-tag size="medium" type="success">作者：</el-tag> {{currentPoetry.author}}</p> <br>
            <div class="poe-content  chapterdtail" v-html="currentPoetry.content"></div>
        </el-card>
            </el-col>
    <el-col :span="10">
        <div class="block" style="overflow: hidden;width:550px" id="comments">
          <div id="input_comments" >
          	  <editorelem style="background-color:#FFF5EE"
                :key="editorelem_key"  :catchData="catchCommentData" :editorindex="1000">
              </editorelem>
            <!-- <el-input type="textarea" :rows="3" placeholder="请输入笔记内容" v-model="newcommet"> </el-input> -->
            <el-button type="success" plain icon="el-icon-circle-plus-outline" @click="new_comment">提交</el-button>
          </div>
          <div class="demo_line_01"><b><span>随笔：</span></b> </div> 
        <div>
        <div id="chaptercomments" style="max-height: 600px;overflow-y: auto; overflow-x: hidden;">
          <el-card v-for="comment in comments_list" :key="comment.id" :body-style="{ 'padding': '15px 15px  5px 15px ' }" >
            <div id="chaptercontent" class="comment" v-html="comment.comments"></div>
            <HR style="border:1 dashed " width="100%" color=#ddd  SIZE=1 />
            <div  class="comment-head "  >
              <span ><el-tag >{{fromat_date(comment.created_at)}}</el-tag></span>
              <el-button style="float: right; padding: 3px 0" type="text" @click="delete_comment(comment)" >
                <i class="el-icon-delete"></i></el-button>
            </div>
          </el-card>
          <el-pagination background v-if="currentPage != 0" @current-change="refresh_data" :current-page.sync="currentPage" 
            :page-size="10" layout="prev, pager, next" :total="comments_count">
          </el-pagination>
        </div>
        </div>
        </div>
    </el-col>
        </el-row>
    </div>
</template>
<script>
import { Poetry, PoetryCommt } from "@/utils/ajaxFunctions";
import editorelem from "@/components/rocky/editor";
import { tools } from "@/utils/tools";
export default {
  name: "poetry-comment",
  data() {
    return {
      poetry_id: this.$route.params.poetry_id,
      token: this.$store.state.token,
      comments_list: [],
      comments_count: 0,
      currentPage: 1,
      currentPoetry: {},
      editorelem_key: new Date().getTime(),
      currentComment: {}
    };
  },
  methods: {
    set_comments(data) {
      this.comments_list = data.results;
      this.comments_count = data.count;
      console.log(JSON.stringify(data.results));
    },
    set_poetry(data) {
      this.currentPoetry = data;
      console.log(this.currentPoetry);
    },
    fromat_date(time) {
      return tools.formatDate(time);
    },
    catchCommentData(val) {
      this.currentComment.comments = val;
    },
    new_comment() {
      console.log(JSON.stringify(this.currentComment));
      PoetryCommt.create_poetry_comm(this.currentComment, this.token, data => {
        this.refresh_data();
      });
    },
    delete_comment(commt) {
      PoetryCommt.delete_poetry_comm(commt, this.token, data => {
        this.refresh_data();
      });
    },
    refresh_data() {
      PoetryCommt.get_poetry_comm(
        this.currentPage,
        this.poetry_id,
        this.token,
        this.set_comments
      );
    }
  },
  created: function() {
    this.currentComment = { poetry_id: this.poetry_id, comments: "" };
    if (this.poetry_id) {
      PoetryCommt.get_poetry_comm(
        this.currentPage,
        this.poetry_id,
        this.token,
        this.set_comments
      );
      Poetry.get_poetry_byid(this.poetry_id, this.token, this.set_poetry);
    } else {
      this.$router.push("/");
    }
  },
  components: {
    editorelem
  }
};
</script>

<style>
.box-card {
  min-height: 800px;
  width: 100%;
}
/* 分隔线  */
.demo_line_01 {
  position: relative;
  padding: 0 10px 0;
  margin: 20px 0;
  line-height: 1px;
  border-left: 20px solid rgb(197, 196, 196);
  border-right: 450px solid #ddd;
  text-align: center;
}

.comment {
  padding: 5px;
  /* background-color: ivory; */
}

.comment-head {
  margin-top: 10px;
  /* border-top: 1px solid #ebeef5; */
  text-align: left;
}
.chapterdtail {
  width: 100%;
  font-size: 150%;
}
.poe-content {
  color: #0f0f0f;
  font-size: 16px;
  line-height: 200%;
}
</style>
