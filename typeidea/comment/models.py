from django.db import models

# Create your models here.
from blog.models import Post

STATUS_NORMAL = 1
STATUS_DELETE = 0
STATUS_DRAFT = 2
STATUS_ITEMS = {
    (STATUS_NORMAL, "正常"),
    (STATUS_DELETE, "删除")
}


class Comment(models.Model):
    target = models.ForeignKey(Post, verbose_name="评论文章")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    reated_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
