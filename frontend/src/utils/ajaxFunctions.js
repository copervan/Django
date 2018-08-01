import $ from 'jquery'

const Users = {
	// 获取用户列表
	get_device(page,token,callback) {
		var myusers = $.ajax({
			url:"/rocky/device/?page="+page,
			type:"GET",
			contentType: 'application/json'	,
			beforeSend: function(xhr){
				xhr.setRequestHeader("Authorization", token);
			},
			success: function(data){
				// console.log(data)
			},
			error: function(err){
				// console.log(err)
				alert(err)
			}
		}).done(callback)
	},
	// 创建用户
	creat_device(user,token,callback){
		var myusers = $.ajax({
			url:"/rocky/device/",
			type:"POST",
			contentType: 'application/json'	,
			beforeSend: function(xhr){
				xhr.setRequestHeader("Authorization", token);
			},
			data: JSON.stringify(user),
			success: function(data){
				// console.log(data)
			},
			error: function(err){
				// console.log(err)
				alert(err,"创建用户失败")
			}
		}).done(callback)
	},
	// 删除用户
	delete_user(user,token,callback) {
    	$.ajax({
			url:"/rocky/device/"+user.id+"/",
			type:"DELETE",
			contentType: 'application/json'	,
			beforeSend: function(xhr){
				xhr.setRequestHeader("Authorization", token);
			},
			error: function(err){
				// console.log(err)
				alert(err,"删除失败")
			}
    	}).done(callback)
    },
    // 编辑用户
    edit_user(user,token,callback) {
    	$.ajax({
			url:"/rocky/device/"+user.id+"/",
			type:"PUT",
			contentType: 'application/json'	,
			beforeSend: function(xhr){
				xhr.setRequestHeader("Authorization", token);
			},
			data: JSON.stringify(user),
			error: function(err){
				// console.log(err)
				alert(err,"修改失败")
			}
    	}).done(callback)
    }
}

const Diarys = {
	get_diary(token,callback) {
		var myusers = $.ajax({
			url:"/rocky/diary/",
			type:"GET",
			contentType: 'application/json'	,
			beforeSend: function(xhr){
				xhr.setRequestHeader("Authorization", token);
			},
			success: function(data){
				// console.log(JSON.stringify(data) )
				// callback =  data
			},
			error: function(err){
				// console.log(err)
				alert(err)
			}
		}).done(callback)
	},
	create_diary(diary,token,callback) {
		$.ajax({
			url:"/rocky/diary/",
			type:"POST",
			contentType: 'application/json'	,
			beforeSend: function(xhr){
				xhr.setRequestHeader("Authorization", token);
			},
			data: JSON.stringify(diary),
			success: function(data){
				// console.log(data)
			},
			error: function(err){
				// console.log(err)
				alert(err)
			}
		}).done(callback)
	}
}

export {Diarys, Users}