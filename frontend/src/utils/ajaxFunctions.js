// import $ from 'jquery'
import axios from 'axios'
import {Message} from 'element-ui'

axios.defaults.timeout = 5000
axios.defaults.headers.post['Content-Type'] = 'application/json'
axios.defaults.headers.get['Content-Type'] = 'application/json'
axios.defaults.headers.put['Content-Type'] = 'application/json'
axios.defaults.headers.delete['Content-Type'] = 'application/json'


//响应拦截器即异常处理
axios.interceptors.response.use(response => {
    return response
}, err => {
    if (err && err.response) {
      switch (err.response.status) {
        case 400:
          err.message = '错误请求'
          Message.error(err.message)
          break;
        case 401:
          err.message = '未授权，请重新登录'
          Message.error(err.message)
          break;
        case 403:
          err.message = '拒绝访问'
          Message.error(err.message)
          break;
        case 404:
          err.message = '请求错误,未找到该资源'
          Message.error(err.message)
          break;
        case 405:
          err.message = '请求方法未允许'
          Message.error(err.message)
          break;
        case 408:
          err.message = '请求超时'
          Message.error(err.message)
          break;
        case 500:
          err.message = '服务器端出错'
          Message.error(err.message)
          break;
        case 501:
          err.message = '网络未实现'
          Message.error(err.message)
          break;
        case 502:
          err.message = '网络错误'
          Message.error(err.message)
          break;
        case 503:
          err.message = '服务不可用'
          Message.error(err.message)
          break;
        case 504:
          err.message = '网络超时'
          Message.error(err.message)
          break;
        case 505:
          err.message = 'http版本不支持该请求'
          Message.error(err.message)
          break;
        default:
          err.message = `连接错误${err.response.status}`
          Message.error(err.message)
      }
    } else {
      err.message = "连接到服务器失败"
      Message.error(err.message)
    }
    message.err(err.message)
    return Promise.resolve(err.response)
})



const Users = {
	// 获取用户列表
	get_device(page,token,callback) {
		axios({
		  method: "GET",
		  url: "/rocky/device/?page="+page,
		  // data: JSON.stringify(diary),
		  headers: {"Authorization":token } 
		}).then(response=>{
				// console.log(response)
				callback(response.data)} )
	},
	// 创建用户
	creat_device(user,token,callback){
		axios({
		  method: "POST",
		  url: "/rocky/device/",
		  data: JSON.stringify(user),
		  headers: {"Authorization":token } 
		}).then(response=>{
				// console.log(response)
				Message.success("用户创建成功")
				callback(response.data)} )
	},
	// 删除用户
	delete_user(user,token,callback) {
		axios({
		  method:"DELETE",
		  url: "/rocky/device/"+user.id+"/",
		  data: JSON.stringify(user),
		  headers: {"Authorization":token } 
		}).then(response=>{
				Message.success("用户删除成功")
				callback(response.data)} )
    },
    // 编辑用户
    edit_user(user,token,callback) {
    	axios({
		  method:"PUT",
		  url: "/rocky/device/"+user.id+"/",
		  data: JSON.stringify(user),
		  headers: {"Authorization":token } 
		}).then(response=>{
				Message.success("用户修改成功")
				callback(response.data)} )
    }
}

const Diarys = {
	get_diary(page,token,callback) {
		axios({
		  method: "GET",
		  url: "/rocky/diary/?page="+page,
		  // data: JSON.stringify(diary),
		  headers: {"Authorization":token } 
		}).then(response=>{
				// console.log(response)
				callback(response.data)} )
	},
	create_diary(diary,token,callback) {
		axios({
		  method: "POST",
		  url: "/rocky/diary/",
		  data: JSON.stringify(diary),
		  headers: {"Authorization":token } 
		}).then(response=>{
				// console.log(response)
				callback(response.data)} )
	}
}

const Notice = {
	get_notice(page,token,callback){
		axios.get('/rocky/notice/today_notice/',
			{ headers: {"Authorization":token} }
			).then(response=>{
				//console.log(response)
				callback(response.data)} )
	},
	create_notice(notice,token,callback){
		axios({
		  method: 'post',
		  url: '/rocky/notice/',
		  data: JSON.stringify(notice),
		  headers: {"Authorization":token } 
		}).then(response=>{
				// console.log(response)
				callback(response.data)} )
	},
	edit_notice(notice,token,callback){
		axios({
		  method: 'put',
		  url: '/rocky/notice/'+notice.id+"/",
		  data: JSON.stringify(notice),
		  headers: {"Authorization":token } 
		}).then(response=>{
				// console.log(response)
				callback(response.data)} )
	},
	all_notice(page,token,callback) {
		axios({
		  method: 'get',
		  url: '/rocky/notice/?page='+page,
		  //data: JSON.stringify(notice),
		  headers: {"Authorization":token} 
		}).then(response=>{
				// console.log(response)
				callback(response.data)} )
	}
}

export {Diarys, Users, Notice}