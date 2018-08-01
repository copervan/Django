
<script type="text/javascript">
	import {Diarys} from '../../utils/ajaxFunctions'
	export default {
		name: 'diary',
		data () {
			return {
				diary_list: [],
				currentdiary : {title:'',content:""},
				diary_add : false,
				columns1: [
					{
						title: "id",
						key : "id"
					},
					{
						title: "title",
						key : "title"
					},
					{
						title: "content",
						key : "content"
					}],
				diary_show: false,
				token: this.$store.state.token,
				currentPage: 1,
				diary_count:0
			}
		},
		methods: {
			set_diary_list(data){
				this.diary_list = data.results
				this.diary_count = data.count
				// console.log(this.diary_list)
			},
			new_diary(){
				this.currentdiary = {title:'',content:""}
				this.diary_add = true
			},
			add_diary(){
				var _this = this
				if(_this.currentdiary.content != '' && _this.currentdiary.title != ''){
					// console.log(_this.currentdiary)
					Diarys.create_diary(_this.currentdiary,_this.token, function(){
							alert("Diary successfully created!")
							Diarys.get_diary(_this.currentPage, _this.token, _this.set_diary_list)
					})
				}
				else {
					alert("标题和内容均不能为空")
				}
				this.diary_add = false
			},
	    	show_detail(index, row) {
            	this.currentdiary =  row
            	this.diary_show = true
		    },
		    handleDblClick(row){
		    	this.currentdiary =  row
		    	this.diary_show = true
		    },
		    handleCurrentChange() {
				var _this = this
				Diarys.get_diary(_this.currentPage, _this.token, _this.set_diary_list)
			},
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
		created: function() {
			// console.log('this is the create' )
			Diarys.get_diary(this.currentPage,this.token, this.set_diary_list)
		},
		computed: {
			my_list : function() {
				// console.log('this is the computed' )
				// console.log(this.diary_list)
				return this.diary_list
			}		
		}
	}
</script>


<template>
	<div>
		<Button type="primary" @click="new_diary">Create The Diary</Button>
<template>
<div>
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

	    <Modal
	        v-model="diary_add"
	        title="Create the diary"
	        :loading="loading"
	        @on-ok="add_diary">
		    <template>
				<Form :model="formTop" label-position="left" >
			        <FormItem label="标题">
			            <Input v-model="currentdiary.title"></Input>
			        </FormItem>
			        <quill-editor ref="myTextEditor"
					    v-model="currentdiary.content" 
					    :config = "editorOption">
					</quill-editor>
			    </Form>
			</template>
	    </Modal>

	    <Modal
	        v-model="diary_show"
	        title="Show diary Detail"
	        :loading="loading"
	        @on-ok="diary_show = false">
		    <template>
				<div style="background:#eee;padding: 20px">
				    <Card :bordered="false">
				        <p slot="title">{{currentdiary.title}}</p>
				        <p style="text-indent:2em"  v-html="currentdiary.content"></p>
				    </Card>
				    <br/>
				    <p>日期：{{formatDate(currentdiary.date) }}</p>
				</div>
			</template>
	    </Modal> 
	</div>
</template>