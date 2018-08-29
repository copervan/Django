<template>
  <div>
  	<el-button  type="success" size="mini" @click="refresh_before" >BEFORE</el-button>
  	<el-input v-model="image_index"></el-input>
    <div v-html="image" @click="refresh_image"></div>
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
			refresh_image(){
				if (this.image_index >=1) {
					this.image_index = this.randomNum(1,1300)
				}
				else {
					this.image_index = 1
				}
			},
			zfill(str){
			    str ='00000'+str;
			    return str.substring(str.length-5);
			},
			randomNum(min,max){ 
			    switch(arguments.length){ 
			        case 1: 
			            return Math.floor(Math.random()*minNum+1); 
			        break; 
			        case 2: 
			            return Math.floor(Math.random()*(max-min+1)+min); 
			        break; 
			            default: 
			                return 0; 
			            break; 
			    } 
			} 
		},
		computed: {
			image: function(){
				return '<img style="width:80%;height:100%" index="'+this.image_index+'"  src="http://192.168.31.101/image/'+this.zfill(this.image_index)+'.jpg" >'
			}
		}
	}

</script>