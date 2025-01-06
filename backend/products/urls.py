from django.urls import path, include
from .views import index
# Добавляем наши urls, точнее домашюю страницу, smart_selects для работы с зависимыми полями в Django админке
urlpatterns = [
    path('my/<int:id>/', index)
]