<template>
	<div>
		<div v-for="diary in my_list" :key="diary.id">
		    <div style="background:#eee;padding: 20px" v-on:click="show_detail(diary)" >
		        <Card :bordered="false" >
		            <p slot="title">{{diary.title}}</p>
		            <p>{{diary.content}}</p>
		            <p>{{diary.date}}</p>
		        </Card>
		    </div>
		</div>
		<Modal
	        v-model="diary_show"
	        title="Create the diary"
	        :loading="loading"
	        @on-ok="diary_show = false">
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
	export default{
		name: 'showdiary',
		props:['my_list'],
		data(){
			return {
				 currentdiary : {title:'',content:""},	
				 diary_show: false		
			}
		},
		methods: {
			showdiary(diary){
				this.currentdiary = diary
				this.diary_show = true
			}
		}
	}
</script>