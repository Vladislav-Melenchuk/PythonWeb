from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_news, name='category_news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]
