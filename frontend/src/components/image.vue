<template>
  <div>
	<mt-loadmore :top-method="loadTop" :bottom-method="loadBottom" :bottom-all-loaded="allLoaded" ref="loadmore">
	  <div id="container">
	  <ul>
	    <li v-for="(item,index) in image_list" :key="index+image_page*10" >
	      <img v-lazy.container="item">
	    </li>
	  </ul>
	</div>
	<el-button style="width: 100%" type="primary" @click="loadBottom">Buttom</el-button>
	</mt-loadmore>


<!--   	<el-button  type="success" size="mini" @click="refresh_before" >BEFORE</el-button>
  	<el-input v-model="image_index"></el-input>
    <div v-html="image" @click="refresh_image"></div>
    <el-button  type="success" size="mini" @click="refresh_after" >AFTER</el-button> -->
  </div>
</template>

<script type="text/javascript">
	export default {
		name: "myimage",
		data() {
			return {
				image_index:1,
				image_page:1,
				allLoaded: false
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
					this.image_index = this.randomNum(1,120)
				}
				else {
					this.image_index = 1
				}
			},
			loadTop() {
			  
			  // 加载更多数据
			  this.image_page = this.randomNum(1,140) 
			  if (this.image_page > 142){
			  	this.allLoaded = true
			  }
			  this.$refs.loadmore.onTopLoaded();
			},
			loadBottom() {

			  // 加载更多数据
			  this.image_page = this.randomNum(1,140) 
			  if (this.image_page > 142){
			  	this.allLoaded = true
			  }
			  //this.allLoaded = true;// 若数据已全部获取完毕
			  this.$refs.loadmore.onBottomLoaded();
			  //console.log(this.image_list)
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
			image_list : function() {
				let id_start = this.image_page * 10
				let id_end = id_start + 10
				let list  = new Array()
				for (let i = id_start ; i < id_end ; i++ ){
					let img = 'http://192.168.31.101/image/'+this.zfill(i)+'.jpg'
					list.push(img)
				}
				console.log(list)
				return list
			},
			images: function(){
				return '<img style="width:80%;height:100%" index="'+this.image_index+'"  src="http://192.168.31.101/image/'+this.zfill(this.image_index)+'.jpg" >'
			}
		}
	}

</script>

<style type="text/css">
img {
  width: 100%;
  margin: auto;
}
</style>