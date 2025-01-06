from django.db import models

from djangocms_text_ckeditor.fields import HTMLField
# from smart_selects.db_fields import ChainedForeignKey

from parler.models import TranslatableModel, TranslatedFields

class News(TranslatableModel):
    NEWS_TYPE_CHOICES = [
        ('行业动态', '行业动态'),
        ('公司新闻', '公司新闻'),
    ]
    image = models.ImageField(verbose_name='新闻图片', upload_to='news/')
    
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    is_published = models.BooleanField(verbose_name='是否发布', default=True)
    translations = TranslatedFields(
        name = models.CharField(verbose_name='新闻标题', max_length=100),
        description = models.CharField(verbose_name='新闻简述', max_length=1000),
        content = HTMLField(verbose_name='新闻内容', blank=True),
        tag=models.CharField(choices=NEWS_TYPE_CHOICES, default='公司新闻',max_length=1000),
    )
    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        db_table = 'news'
        ordering = ['-created_at']
