<template>
	<div>
		<Button type="primary" @click="diary_add = true">create a diary</Button>
		<div v-for="diary in diary_list">
		    <div style="background:#eee;padding: 20px" v-on:click="show_detail(diary)" >
		        <Card :bordered="false" >
		            <p slot="title">{{diary.title}}</p>
		            <p>{{diary.content}}</p>
		            <p>{{diary.date}}</p>
		        </Card>
		    </div>
    	</div> 
	    <Modal
	        v-model="diary_add"
	        title="Create the diary"
	        :loading="loading"
	        @on-ok="add_diary">
	        <p>After you click ok, the dialog box will close in 2 seconds.</p>
		    <template>
				<Form :model="formLeft" label-position="top" :label-width="300">
			        <FormItem label="title">
			            <Input v-model="currentdiary.title"></Input>
			        </FormItem>
			        <FormItem label="content">
			            <Input v-model="currentdiary.content" type="textarea" :autosize="{minRows: 5,maxRows: 15}" placeholder="Enter something..."></Input>
			        </FormItem>
			    </Form>
			</template>
	    </Modal>
	</div>
</template>

<script type="text/javascript">
	import $ from 'jquery'
	export default {
		name: 'diary',
		data () {
			return {
				diary_list: [],
				currentdiary : {title:'',content:""},
				diary_add : false
			}
		},
		methods: {
			diary_list: function(){

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
				var _this =  this 
				//var diary_list = this.diary_list
				//_this.currentdiary = {title:'',content:""},
				this.create_diary(this.currentdiary, function(){
					alet("Diary successfully created!")
					_this.get_diary(function(data) {
						this.diary_list.push(data)
						console.log(_this.diary_list)
					})
					_this.diary_add = false
				})
			}

		},
		created : function() {
			this.get_diary(function(data) {
				this.diary_list = data
				this.$nextTick()
				console.log(this.diary_list)
			})
		}
	}
</script>