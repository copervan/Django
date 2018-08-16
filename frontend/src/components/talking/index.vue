<template>
	<div id="talkingroom">
		<div id="messageShow">
			
		</div>
		<div id="messageForm">
			<el-input type="text" name="message" v-bind:message>
			<el-button style="float: right;" type="success" size="mini" @click="refresh_data" >OK</el-button>
		</div>
	</div>
</template>

<script type="text/javascript">
import '@/utils/mqttws31'
export default {
	name: 'talking',
	data(){
		client: new Paho.MQTT.Client('172.16.0.23',1883,"123"),
		topic: "mqtt"
	}
	methods: {
	onConnectionLost: function (responseObject) {
		if (responseObject.errorCode !== 0) {
			console.log('onConnectionLost:' + responseObject.errorMessage);
			console.log('连接已断开');
		}
	},
	onMessageArrived: function(message) {
	  	console.log("收到消息:"+message.payloadString);
	},
	onConnect: function() {
	  	console.log('onConnected');
	  	this.client.subscribe(this.topic); // 订阅主题
	}
	},
	created: function() {
		this.client.connect({onSuccess: this.onConnect}); // 连接服务器并注册连接成功处理事件
		this.client.onConnectionLost = this.onConnectionLost; // 注册连接断开处理事件
		this.client.onMessageArrived = this.onMessageArrived; // 注册消息接收处理事件
		// this.client.disconnect(); // 断开连接
	}
} 
</script>