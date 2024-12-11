from django.db import models

from djangocms_text_ckeditor.fields import HTMLField
# from smart_selects.db_fields import ChainedForeignKey



class Product(models.Model):
    photo = models.ImageField(verbose_name='产品图片', upload_to='products/')
    name = models.CharField(verbose_name='产品名称', max_length=100)
    description = HTMLField(verbose_name='产品详情', blank=True)
    price = models.PositiveIntegerField(verbose_name='价格')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    is_published = models.BooleanField(verbose_name='是否发布', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'
        db_table = 'products'
        ordering = ['-created_at']
