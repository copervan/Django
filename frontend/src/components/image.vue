<template>
  <div>
  	<el-button  type="success" size="mini" @click="refresh_before" >BEFORE</el-button>
    <div v-html="image" @click="refresh_after"></div>
    <el-button  type="success" size="mini" @click="refresh_after" >AFTER</el-button>
  </div>
</template>

<script type="text/javascript">
	export default {
		name: "image",
		data() {
			return {
				image_index:1,
				// image: '<img src="http://192.168.1.100/image/00001.jpg">'
			}
		},
		methods:{
			refresh_before(){
				if (this.image_index >=2) {
					this.image_index = this.image_index - 1
				}
				else {
					this.image_index = 1
				}
			},
			refresh_after(){
				if (this.image_index >=1) {
					this.image_index = this.image_index +1
				}
				else {
					this.image_index = 1
				}
			},
			zfill(str){
			    str ='00000'+str;
			    return str.substring(str.length-5);
			}
		},
		computed: {
			image: function(){
				return '<img style="width:80%;height:100%" index="'+this.image_index+'"  src="http://192.168.1.100/image/'+this.zfill(this.image_index)+'.jpg" >'
			}
		}
	}

</script>