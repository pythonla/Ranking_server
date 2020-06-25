from django.db import models

# Create your models here.


class Client(models.Model):
    """地址"""
    number = models.CharField(max_length=20, verbose_name="客户端号")
    receiver_mobile = models.IntegerField( verbose_name="分数")

    class Meta:
        db_table = "client_ranking"