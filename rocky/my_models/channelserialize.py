from rest_framework import serializers 
from .channel import Channel , ChannelBed, ChannelDevice, ChannelUser

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ("id", "name", "project_id", "province", "city", "created_at",  "updated_at" )

class ChannelBedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelBed
        fields = ("id", "channel_id", "project_id", "room_id", "bed_num", "device_no", 
                  "person_id","remark", "created_at",  "updated_at"  )


class ChannelDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelDevice
        fields = ("id", "device_no" ,"project_id", "channel_id", "user_name", "created_at",  "updated_at"  )

class ChannelUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "channel_id" ,"project_id", "email", "real_name",  "last_login_ip" 
                  , "last_login_at", "status", "created_at",  "updated_at" )
        