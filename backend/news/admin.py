from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import News

class NewsAdmin(TranslatableAdmin):
    list_display = ('id','name', 'description')
    def custom_description(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    custom_description.short_description = 'Description Preview' 

admin.site.register(News, NewsAdmin)
