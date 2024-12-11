from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from backend.plugins.module_name import MODULE_NAME

from . import models


class ProductPlugin(CMSPluginBase):
    model = models.ProductModel
    module = MODULE_NAME
    name = _("product")
    render_template = 'product_plugin/plugins/product.html'
    allow_children = True


plugin_pool.register_plugin(ProductPlugin)
