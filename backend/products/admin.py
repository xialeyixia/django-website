from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'description')
    # list_display_links = ['id', 'name']
    # search_fields = ['id', 'name', 'price', 'product_category']
    def custom_description(self, obj):
        # 这里可以添加任何你想要的格式化逻辑
        # 例如，截取description字段的前100个字符
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    custom_description.short_description = 'Description Preview' 

admin.site.register(Product, ProductAdmin)

