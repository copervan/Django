
<script type="text/javascript">
import { Diarys } from "@/utils/ajaxFunctions";
import editorelem from "./editor";

export default {
  name: "diary",
  data() {
    return {
      diary_list: [],
      currentdiary: { title: "", content: "", editor: new Date().getTime() },
      diary_add: false,
      columns1: [
        {
          title: "id",
          key: "id"
        },
        {
          title: "title",
          key: "title"
        },
        {
          title: "content",
          key: "content"
        }
      ],
      diary_show: false,
      token: this.$store.state.token,
      currentPage: 1,
      diary_count: 0
    };
  },
  methods: {
    // 钩子函数，用于为属性赋值
    set_diary_list(data) {
      this.diary_list = data.results;
      this.diary_count = data.count;
      // console.log(this.diary_list)
    },
    // 响应点击“添加”
    new_diary() {
      // 设置editor 的key元素，更新key值，以达到刷新组件的目的。
      this.currentdiary = {
        title: "",
        content: "",
        editor: new Date().getTime()
      };
      this.diary_add = true;
    },
    // 响应点击“添加”后的提交
    add_diary() {
      var _this = this;
      if (_this.currentdiary.content != "" && _this.currentdiary.title != "") {
        // console.log(_this.currentdiary)
        Diarys.create_diary(_this.currentdiary, _this.token, data => {
          // alert("Diary successfully created!")
          this.$message({
            message: "Diary successfully created!",
            center: true,
            type: "success"
          });
          Diarys.get_diary(
            _this.currentPage,
            _this.token,
            _this.set_diary_list
          );
          _this.diary_add = false;
        });
      } else {
        // alert("标题和内容均不能为空")
        this.$alert("标题和内容均不能为空", "", {
          confirmButtonText: "确定",
          callback: action => {}
        });
      }
      this.diary_add = false;
    },
    // 响应点击“查看”
    show_detail(index, row) {
      this.currentdiary = row;
      this.diary_show = true;
    },
    // 响应双击事件
    handleDblClick(row) {
      this.currentdiary = row;
      this.diary_show = true;
    },
    // 刷新页面 响应分页 与refresh_data 重复
    handleCurrentChange() {
      var _this = this;
      Diarys.get_diary(_this.currentPage, _this.token, _this.set_diary_list);
    },
    // 格式化时间输出，可以写成功能函数， 有时间再弄
    formatDate(time) {
      var date = new Date(time);

      var year = date.getFullYear(),
        month = date.getMonth() + 1, //月份是从0开始的
        day = date.getDate(),
        hour = date.getHours(),
        min = date.getMinutes(),
        sec = date.getSeconds();
      var newTime =
        year +
        "-" +
        (month < 10 ? "0" + month : month) +
        "-" +
        (day < 10 ? "0" + day : day) +
        " " +
        (hour < 10 ? "0" + hour : hour) +
        ":" +
        (min < 10 ? "0" + min : min) +
        ":" +
        (sec < 10 ? "0" + sec : sec);

      return newTime;
    },
    // 响应点击“刷新” 方法重复了
    refresh_data() {
      Diarys.get_diary(this.currentPage, this.token, this.set_diary_list);
    },
    // 该方法将传递给editor，子组件调用该方法传递子组件的参数至父组件。
    catchData(value) {
      this.currentdiary.content = value; //在这里接受子组件传过来的参数，赋值给data里的参数
    }
  },
  created: function() {
    // console.log('this is the create' )
    // 调用接口，初始化内容
    Diarys.get_diary(this.currentPage, this.token, this.set_diary_list);
  },
  computed: {
    my_list: function() {
      // console.log('this is the computed' )
      // console.log(this.diary_list)
      return this.diary_list;
    }
  },
  // 使用自定义组件做页面标签时必须在此处进行注册，否则无法识别
  components: {
    editorelem
  }
};
</script>

<template>
	<div><br/>
		<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
          @click="new_diary">Create The Diary</el-button>
		<el-button style="float: right;" type="success" size="mini" @click="refresh_data" >刷新</el-button>
<template>
<div>
	<br/>
  <el-table
    :data="my_list"
    highlight-current-row
    @row-dblclick="handleDblClick"
    style="width: 100%">
    <el-table-column
      label="ID"
      width="180">
      <template slot-scope="scope">
        <i class="el-icon-info"></i>
        <span style="margin-left: 10px">{{ scope.row.id }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="标题"
      width="180">
      <template slot-scope="scope">
        <i class="el-icon-tickets"></i>
        <span style="margin-left: 10px">{{ scope.row.title}}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="日期"
      width="180">
      <template slot-scope="scope">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ formatDate(scope.row.date) }}</el-tag>
          </div>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini" icon="el-icon-view"
          @click="show_detail(scope.$index, scope.row)">查看</el-button>
      </template>
    </el-table-column>
  </el-table>
    <div class="block">
    <el-pagination
      @current-change="handleCurrentChange"
      :current-page.sync="currentPage"
      :page-size="10"
      layout="total, prev, pager, next"
      :total="diary_count">
    </el-pagination>
  </div>
</div>
</template>		

	    <el-dialog
	        :visible.sync="diary_add"
	        title="Create the diary"
	        @on-ok="add_diary">
		    <template>
				<el-form label-position="left" >
			        <el-form-item label="标题">
			            <el-input v-model="currentdiary.title"></el-input>
			        </el-form-item>
			        <!-- 使用富文本编辑器，做博文输入 -->
			        <editorelem :key="currentdiary.editor" :catchData="catchData"  ></editorelem>
<!-- 			        <quill-editor ref="myTextEditor"
					    v-model="currentdiary.content" 
					    :config = "editorOption">
					</quill-editor> -->
			    </el-form >
			</template>
			<div slot="footer" class="dialog-footer">
			  <el-button @click="diary_add = false">取 消</el-button>
			  <el-button type="primary" @click="add_diary()">提交</el-button>
			</div>
	    </el-dialog>

	    <el-dialog
	        :visible.sync="diary_show"
	        title="Show diary Detail"
	        @on-ok="diary_show = false">
		    <template>
				    <el-card :bordered="false" style="background:#FFFFF0">
				        <h2 slot="header">{{currentdiary.title}}</h2>
				        <!-- <p style="text-indent:2em"  v-html="currentdiary.content"></p> -->
				        <p   v-html="currentdiary.content"></p>
				    </el-card>
				    <br/>
				    <p>日期：{{formatDate(currentdiary.date) }}</p>
			</template>
	    </el-dialog> 
	</div>
</template>