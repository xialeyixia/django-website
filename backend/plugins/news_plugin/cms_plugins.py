from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from backend.plugins.module_name import MODULE_NAME

from . import models


class NewsPlugin(CMSPluginBase):
    model = models.NewsModel
    module = MODULE_NAME
    name = _("news")
    render_template = 'news_plugin/plugins/news.html'
    # allow_children = True
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        print(context, instance, 8888)
        return context


plugin_pool.register_plugin(NewsPlugin)
