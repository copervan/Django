
<script type="text/javascript">
import { Users } from "@/utils/ajaxFunctions";
import { mapState } from "vuex";
import login from "./login";
export default {
  name: "home",
  data() {
    return {
      users1: [],
      user_count: 0,
      currentPage: 1,
      columns1: [
        {
          title: "id",
          key: "id"
        },
        {
          title: "username",
          key: "username"
        },
        {
          title: "email",
          key: "email"
        },
        {
          title: "first_name",
          key: "first_name"
        },
        {
          title: "last_name",
          key: "last_name"
        }
      ],
      formLeft: {
        input1: "",
        input2: "",
        input3: ""
      },
      modal6: false,
      edituser: false,
      loading: true,
      currentuser: {},
      token: this.$store.state.token, 

      newuser: {
        username: "",
        password: "",
        email : "",
        first_name: "",
        last_name: "" ,
      },
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 5, max: 16, message: "长度在 5 到 16 个字符", trigger: "blur" }
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { min: 5, max: 16, message: "长度在 5 到 16 个字符", trigger: "blur" }
        ],
        email : [
          { type:"email", required: true, message: "请输入邮箱", trigger: "blur" },
        ],
        first_name: [
          { required: true, message: "请输入first_name", trigger: "blur" },
          { max: 16, message: "长度在16 个字符以内", trigger: "blur" }
        ],
        last_name: [
          { required: false, message: "请输入last_name", trigger: "blur" },
          { max: 16, message: "长度在 16 个字符以内", trigger: "blur" }
        ],
      },
      
    };
  },
  methods: {
    setusers(data) {
      // console.log(data)
      this.users1 = data.results;
      this.user_count = data.count;
    },
    asyncOK(newuser) {
      this.$refs[newuser].validate(valid => {
        if (valid) {
          Users.create_user(this.newuser, this.token, data => {
            this.refresh_data() ;
            this.modal6 = false ;
          }) ;
        }
        else {
          this.$message.error("ERROR: Invalid Usermane or Password !");
        }
      });
    },
    creat_user() {
      this.newuser =  {
        username: "",
        password: "",
        email : "",
        first_name: "",
        last_name: "" ,
      },
      this.modal6 = true;
    },
    submmit_edit() {
      // console.log(_this.token)
      Users.edit_user(this.currentuser, this.token, data => {
        this.refresh_data()
        this.edituser = false;
      });
    },
    delete_user() {
      var _this = this;
      // console.log(_this.token)
      Users.delete_user(_this.currentuser, _this.token, function() {
        Users.get_device(_this.currentPage, _this.token, _this.setusers);
      });
    },
    handleEdit(index, row) {
      // console.log(row)
      this.currentuser = JSON.parse(JSON.stringify(row));
      // console.log(this.currentuser)
      this.edituser = true;
    },
    handleDelete(index, row) {
      // console.log(row)
      this.currentuser = JSON.parse(JSON.stringify(row));
      // console.log(this.currentuser)
      this.delete_user();
    },
    handleCurrentChange() {
      var _this = this;
      Users.get_device(_this.currentPage, _this.token, _this.setusers);
    },
    refresh_data() {
      Users.get_device(this.currentPage, this.token, this.setusers);
    }
  },
  created: function() {
    Users.get_device(this.currentPage, this.token, this.setusers);
  },
  computed: {
    data1: function() {
      // console.log(this.users1)
      return this.users1;
    }
  }
};
</script>


<template>
	<div>
		<h1>Hello Rocky</h1>
		<P>这是主页</P><br/>
		<div v-if="users1">
		<el-button type="success" plain
          size="mini" icon="el-icon-circle-plus-outline"
          @click="creat_user">创建用户</el-button> 
        <el-button style="float: right;" type="primary" plain size="mini" @click="refresh_data" >刷新</el-button>
<!-- 			<Button type="primary" @click="creat_user">创建用户</Button> -->
			<!-- <Table highlight-row ref="currentRowTable" @on-current-change="select_current_user"  -->
				<!-- @on-row-dblclick="row_dblclick" :columns="columns1" :data="data1"></Table> -->
		<!-- 用户列表模块 -->
		<template>
			<div>
				<br/>
			<el-table
			:data="data1" border
			style="width: 100%">
			<el-table-column
			  label="ID"
			  width="180">
			  <template slot-scope="scope">
			    <i class="el-icon-time"></i>
			    <span style="margin-left: 10px">{{ scope.row.id }}</span>
			  </template>
			</el-table-column>
			<el-table-column
			  label="Username"
			  width="180">
			  <template slot-scope="scope">
			    <i class="el-icon-lx-peoplefill"></i>
			    <span style="margin-left: 10px">{{ scope.row.username }}</span>
			  </template>
			</el-table-column>
			<el-table-column
			  label="Email"
			  width="180">
			  <template slot-scope="scope">
			      <div slot="reference" class="name-wrapper">
			        <i class="el-icon-lx-mail"></i>
              <span style="margin-left: 10px">{{ scope.row.email }} </span>
			      </div>	
			  </template>
			</el-table-column>
      <el-table-column
			  label="First Name"
			  width="180">
			  <template slot-scope="scope">
			      <div slot="reference" class="name-wrapper">
			        {{ scope.row.first_name }}
			      </div>
			  </template>
			</el-table-column>
      <el-table-column
			  label="Last Name"
			  width="180">
			  <template slot-scope="scope">
			      <div slot="reference" class="name-wrapper">
              {{ scope.row.last_name }}
			      </div>
			  </template>
			</el-table-column>
			<el-table-column label="操作">
			  <template slot-scope="scope">
			    <el-button
			      size="mini" icon="el-icon-edit"
			      @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
			    <!-- <el-button
			      size="mini"
			      type="danger" icon="el-icon-delete"
			      @click="handleDelete(scope.$index, scope.row)">删除</el-button> -->
			  </template>
			</el-table-column>
			</el-table>
			<div class="block">
			<el-pagination
			  @current-change="handleCurrentChange"
			  :current-page.sync="currentPage"
			  :page-size="10"
			  layout="total, prev, pager, next"
			  :total="user_count">
			</el-pagination>
			</div>
			</div>
		</template>

    <!-- 创建用户表单 -->
		</div>
		<el-dialog title="Create User" :visible.sync="modal6">
		  <el-form label-position="left" :model="newuser" :rules="rules" ref="newuser"  >
        <el-form-item label="user_name:" prop="username">
		    	<el-input v-model="newuser.username"></el-input>
		    </el-form-item>
        <el-form-item label="email:" prop="email">
		    	<el-input v-model="newuser.email"></el-input>
		    </el-form-item>
		    <el-form-item label="password:"  prop="password">
		    	<el-input type="password" v-model="newuser.password"></el-input>
		    </el-form-item>
		    <el-form-item label="first_name:" prop="last_name" >
					<el-input v-model="newuser.first_name" ></el-input>
		    </el-form-item>
        <el-form-item label="last_name:" prop="last_name">
					<el-input v-model="newuser.last_name"></el-input>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="modal6 = false">取 消</el-button>
		    <el-button type="primary" @click="asyncOK('newuser')">确 定</el-button>
		  </div>
		</el-dialog>

		<el-dialog title="edituser" :visible.sync="edituser">
		  <el-form label-position="left" :model="formLeft" :rules="rules" >
        <el-form-item label="user_name:" prop="username"  >
		    	<el-input disabled v-model="currentuser.username"></el-input>
		    </el-form-item>
        <el-form-item label="email:" prop="email"  >
		    	<el-input disabled  v-model="currentuser.email"></el-input>
		    </el-form-item>
        <el-form-item label="first_name:" prop="last_name" >
					<el-input v-model="currentuser.first_name" ></el-input>
		    </el-form-item>
        <el-form-item label="last_name:" prop="last_name">
					<el-input v-model="currentuser.last_name"></el-input>
		    </el-form-item>
		  </el-form>
		  <div slot="footer" class="dialog-footer">
		    <el-button @click="edituser = false">取 消</el-button>
		    <el-button type="primary" @click="submmit_edit">确 定</el-button>
		  </div>
		</el-dialog>
	</div>
</template>