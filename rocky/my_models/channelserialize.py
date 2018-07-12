from rest_framework import serializers 


class ChannelSerializer(serializers.Serializer):
    name = serializers.CharField()
    project_id = serializers.IntegerField() 
    province = serializers.CharField()
    city = serializers.CharField() 
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()  

class ChannelBedSerializer(models.Model):
    channel_id = serializers.IntegerField() 
    project_id = serializers.IntegerField() 
    room_id = serializers.IntegerField() 
    bed_num = models.CharField("床号",max_length=255)
    device_no = serializers.IntegerField() 
    person_id = serializers.IntegerField() 
    remark = models.CharField("备注",max_length=255)
    created_at = serializers.DateTimeField()  
    updated_at = serializers.DateTimeField()  

class ChannelDeviceSerializer(models.Model):
    device_no = models.IntegerField("设备编号", max_length=20)
    project_id = models.IntegerField("项目编号", max_length=20)
    channel_id = models.IntegerField("渠道编号", max_length=20)
    user_name = models.CharField("用户名",max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )

class ChannelUserSerializer(models.Model):
    channel_id = models.IntegerField("渠道编号", max_length=20)
    project_id = models.IntegerField("项目编号", max_length=20)
    email = models.EmailField("用户邮箱")
    password = models.CharField("用户密码", max_length=255)
    real_name = models.CharField("用户名称", max_length=255)
    last_login_ip = models.CharField("上次登录IP", max_length=255)
    last_login_at = models.DateTimeField("上次登录时间", default = timezone.now )
    status = models.IntegerField("", max_length=1)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )