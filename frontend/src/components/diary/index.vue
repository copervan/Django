
<script type="text/javascript">
	import $ from 'jquery'
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
				diary_show: false
			}
		},
		methods: {
			set_diary_list(data){
				console.log(data)
				this.diary_list = data
				console.log(this.diary_list)
			},
			get_diary(callback) {
				var mytoken = this.$store.state.token
				var myusers = $.ajax({
					url:"/rocky/diary/",
					type:"GET",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					success: function(data){
						console.log(JSON.stringify(data) )
						// callback =  data
					},
					error: function(err){
						console.log(err)
						alert(err)
					}
				}).done(callback)
			},
			create_diary(currentdiary,callback) {
				var mytoken = this.$store.state.token
				$.ajax({
					url:"/rocky/diary/",
					type:"POST",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					data: JSON.stringify(currentdiary),
					success: function(data){
						console.log(data)
						// callback =  data
					},
					error: function(err){
						console.log(err)
						alert(err)
					}
				}).done(callback)
			},
			add_diary(){
				//var _this =  this 
				//var diary_list = this.diary_list
				//_this.currentdiary = {title:'',content:""},
				this.create_diary(this.currentdiary, function(){
					alert("Diary successfully created!")
						this.get_diary(this.set_diary_list)
					})
				this.diary_add = false
			},
			select_current_diary(currentRow,oldCurrentRow){
            	console.log(currentRow,oldCurrentRow)
            	this.currentdiary = currentRow
            }

		},
		created: function() {
			console.log('this is the create' )
			this.get_diary(this.set_diary_list)
		},
		computed: {
			my_list : function() {
				console.log('this is the computed' )
				console.log(this.diary_list)
				return this.diary_list
			}		
		}
	}
</script>


<template>
	<div>
		<Button type="primary" @click="diary_add = true">Create The Diary</Button>
		<template>
			<Table highlight-row ref="currentRowTable" @on-current-change="select_current_diary" 
			@on-row-dblclick="diary_show = true" :columns="columns1" :data="my_list"></Table>
		</template>
	    <Modal
	        v-model="diary_add"
	        title="Create the diary"
	        :loading="loading"
	        @on-ok="add_diary">
		    <template>
				<Form :model="formTop" label-position="left" :label-width="500">
			        <FormItem label="title">
			            <Input v-model="currentdiary.title"></Input>
			        </FormItem>
			        <FormItem label="content">
			            <Input v-model="currentdiary.content" type="textarea" :autosize="{minRows: 5,maxRows: 15}" placeholder="Enter something..."></Input>
			        </FormItem>
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
				        <p>{{currentdiary.content}}</p>
				    </Card>
				    <br/>
				    <p>日期：{{currentdiary.date}}</p>
				</div>
			</template>
	    </Modal> 
	</div>
</template>