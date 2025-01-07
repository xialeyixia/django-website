from django.shortcuts import render, get_object_or_404
from .models import News
# Create your views here.
def index(request, id):
    # product = Product.objects.get(id=id)
    news = get_object_or_404(News, id=id)
    related_news = News.objects.filter(tag=news.tag).exclude(id=id)[:5]
    context = {
        'news': news,
        'related_news':related_news
    }
    return render(request, 'backend_news/index.html', context)
