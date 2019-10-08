from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)

    # SlugField字段是将输入的内容中的空格都替换成‘-’之后保存
    tag = models.SlugField
    # 1、设定普通外键 连接ContentType 具体对应的模型
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    # 2、设立一个PoitiveIntegerField字段 记录对应模型的实例的id 具体是哪一篇文章
    object_id = models.PositiveIntegerField()
    # 3、有了模型和模型的实例id(文章id） 设定这个GenericForeignkey外键了
    # 这个外键需要传入两个参数，就是上面的1和2，
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag


class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num

        except exceptions.ObjectDoesNotExist:
            return 0


class ReadDetail(models.Model):
    date = models.DateTimeField(default=timezone.now)
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

