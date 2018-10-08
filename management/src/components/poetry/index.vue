<script>
import { Poetry, PoetryComm } from "@/utils/ajaxFunctions";
import editorelem from "@/components/rocky/editor";
export default {
  name: "poetrys",
  data() {
    return {
      poetry_list: [],
      poetry_count: 0,
      currentPage: 1,
      token: this.$store.state.token,
      poetry_add: false,
      currentPoetry: {
        title: "",
        author: "",
        content: "",
        updated_at: new Date(),
        editor: new Date().getTime()
      },
      dialog_status: "Create"
    };
  },
  methods: {
    set_poetry_list(data) {
      this.poetry_list = data.results;
      this.poetry_count = data.count;
      console.log(JSON.stringify(data.results));
    },
    catchData(val) {
      this.currentPoetry.content = val;
    },
    refresh_data() {
      Poetry.get_poetry(this.currentPage, this.token, this.set_poetry_list);
    },
    view_detail(poetry) {
        this.$router.push("/poetrycommnet/"+poetry.id)
    },
    add_poetry() {
      this.currentPoetry = {
        title: "",
        author: "",
        content: "",
        editor: new Date().getTime()
      };
      this.poetry_add = true;
      this.dialog_status = "Create";
    },
    update_poetry(poetry) {
      this.currentPoetry = {
        title: "",
        author: "",
        content: "",
        editor: new Date().getTime()
      };
      Object.assign(this.currentPoetry, poetry);
      console.log(this.currentPoetry);
      this.poetry_add = true;
      this.dialog_status = "Update";
    },
    handle_submmit() {
      if (this.dialog_status == "Create") {
        Poetry.create_poetry(this.currentPoetry, this.token, data => {
          this.$message({
            message: "创建成功",
            center: true,
            type: "success"
          });
          this.refresh_data();
        });
      } else if (this.dialog_status == "Update") {
        this.currentPoetry.updated_at = new Date();
        // console.log(JSON.stringify(this.the_form));
        Poetry.update_poetry(this.currentPoetry, this.token, data => {
          this.$message({
            message: "更新成功",
            center: true,
            type: "success"
          });
          this.refresh_data();
        });
      }
      this.poetry_add = false;
    }
  },
  created: function() {
    Poetry.get_poetry(this.currentPage, this.token, this.set_poetry_list);
  },
  components: {
    editorelem
  }
};
</script>

<template>
    <div id = "poetry-list">
        <el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
		 @click="add_poetry">新增诗词</el-button>
		<el-button style="float: right;" type="primary" plain  size="mini" @click="refresh_data" >刷新</el-button>
        <el-card v-for="poetry in poetry_list" :key="poetry.id">
            <div slot="header" class="clearfix" @dblclick="update_poetry(poetry)" >
                <span>{{poetry.title}}</span>
                <el-button style="float: right; padding: 3px 0" type="text" @click="view_detail(poetry)">查看详情</el-button>
                <el-button style="float: right; padding: 3px 0" type="text">删除按钮</el-button>
            </div>
            <p><el-tag size="medium" type="success">作者：</el-tag> {{poetry.author}}</p> <br>
            <div class="poe-content" v-html="poetry.content"></div>
        </el-card>
        <el-dialog
	        :visible.sync="poetry_add"
	        :title="this.dialog_status == 'Create' ?  'Create the Poetry' : 'Edit the poetry' "
	    >
		    <template>
				<el-form label-position="left" label-width="80px" >
			        <el-form-item label="标题">
			            <el-input v-model="currentPoetry.title"></el-input>
			        </el-form-item>
                    <el-form-item label="作者">
			            <el-input v-model="currentPoetry.author"></el-input>
			        </el-form-item>
                    <el-form-item label="正文">
			            <!-- 使用富文本编辑器，做博文输入 -->
			            <editorelem :key="currentPoetry.editor" :catchData="catchData" :content="currentPoetry.content" >
                        </editorelem>
			        </el-form-item>
			    </el-form >
			</template>
			<div slot="footer" class="dialog-footer">
			  <el-button @click="poetry_add = false">取 消</el-button>
			  <el-button type="primary" @click="handle_submmit()">提交</el-button>
			</div>
	    </el-dialog>
    </div>
</template>

<style>
.poe-content {
  color: #0f0f0f;
  font-size: 16px;
  line-height: 200%;
}
</style>
