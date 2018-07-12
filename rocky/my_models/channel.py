from django.db import models
from django.utils import timezone 

class Channel(models.Model):
    name = models.CharField("",max_length=255)
    project_id = models.BigIntegerField("项目编号", max_length=20) 
    province = models.CharField("省份的名字",max_length=255)
    city = models.CharField("城市名字",max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )

class ChannelBed(models.Model):
    channel_id = models.BigIntegerField("用户所属渠道", max_length=20)
    project_id = models.BigIntegerField("项目编号", max_length=20)
    room_id = models.BigIntegerField("房间号", max_length=20)
    bed_num = models.CharField("床号",max_length=255)
    device_no = models.BigIntegerField("设备编号", max_length=20)
    person_id = models.BigIntegerField("用户ID",max_length=20 )
    remark = models.CharField("备注",max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default     = timezone.now )

class ChannelDevice(models.Model):
    device_no = models.BigIntegerField("设备编号", max_length=20)
    project_id = models.BigIntegerField("项目编号", max_length=20)
    channel_id = models.BigIntegerField("渠道编号", max_length=20)
    user_name = models.CharField("用户名",max_length=255)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )

class ChannelUser(models.Model):
    channel_id = models.BigIntegerField("渠道编号", max_length=20)
    project_id = models.BigIntegerField("项目编号", max_length=20)
    email = models.EmailField("用户邮箱")
    password = models.CharField("用户密码", max_length=255)
    real_name = models.CharField("用户名称", max_length=255)
    last_login_ip = models.CharField("上次登录IP", max_length=255)
    last_login_at = models.DateTimeField("上次登录时间", default = timezone.now )
    status = models.SmallIntegerField("", max_length=1)
    created_at = models.DateTimeField("创建时间", default = timezone.now )
    updated_at = models.DateTimeField("更新时间", default = timezone.now )
    