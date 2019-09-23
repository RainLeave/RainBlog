from django.db import models

class Mysite(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    author = models.CharField(max_length=100)
    num = models.IntegerField(max_length=10)

    def __str__(self):
        # 这样后台就可以显示模型的每一个title
        return self.title