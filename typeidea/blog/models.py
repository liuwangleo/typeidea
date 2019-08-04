from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_NORMAL = 1
STATUS_DELETE = 0
STATUS_DRAFT = 2
STATUS_ITEMS = {
    (STATUS_NORMAL, "正常"),
    (STATUS_DELETE, "删除")
}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否启用导航")
    owner = models.ForeignKey(User, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者")
    reated_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"


class Post(models.Model):
    STATUS_ITEMS = {
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
        (STATUS_DRAFT, "草稿")
    }
    title = models.CharField(max_length=255, verbose_name="标题")
    desc = models.CharField(max_length=255, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文必须为Markdown格式")
    category = models.ForeignKey(Category, verbose_name="分类")
    tag = models.ForeignKey(Tag, verbose_name="标签")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者")
    reated_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Mate:
        verbose_name = verbose_name_plural = "文章"
        order_by = ["-id"]  # 根据id进行降序排列
