from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from ckeditor.fields import RichTextField


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)

    content = RichTextUploadingField()

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 反向查询 contenttype
    read_details = GenericRelation(ReadDetail)
    readed_num = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']


# class ReadNum(models.Model):
#     read_num = models.IntegerField(dafault=0)
#     blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)