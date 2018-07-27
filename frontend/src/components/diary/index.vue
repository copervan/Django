<template>
	<div>
		<template v-for="diary in diary_list" >
	    <div style="background:#eee;padding: 20px" v-on:click="show_detail(diary)" >
	        <Card :bordered="false" >
	            <p slot="title">{{diary.id}}</p>
	            <p>{{diary.user_name}}</p>
	        </Card>
	    </div>
	    </template>
	</div>
</template>

<script type="text/javascript">
	import $ from 'jquery'
	export default {
		name: 'diary',
		data () {
			return {
				diary_list: []
			}
		},
		methods: {
			get_diary(callback) {
				var mytoken = this.$store.state.token
				var myusers = $.ajax({
					url:"/rocky/device/",
					type:"GET",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
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

		},
		created : function() {
			var _this =  this
			_this.get_diary(function(data) {
				_this.diary_list =  data
				console.log(_this.diary_list)
			})
		}
	}
</script>