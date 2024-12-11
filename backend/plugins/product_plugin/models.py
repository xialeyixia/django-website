from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField
from backend.products.models import Product

class ProductModel(CMSPlugin):
    image = FilerImageField(verbose_name="Image", null=True, blank=True,
                            on_delete=models.SET_NULL, related_name='+')
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,  # 当关联的产品被删除时，设置为 NULL
        null=True,  # 允许为空
        blank=True,  # 在 Django admin 中允许为空字段
        related_name='plugin_product_lists',  # 反向查询的名称
        verbose_name= 'Selected Product'  # 字段的显示名称
    )
    def __str__(self):
        return self.image.label if self.image else "No Image"
