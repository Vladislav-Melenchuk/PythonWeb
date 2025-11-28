from django.shortcuts import render, get_object_or_404
from .models import Category, News

def index(request):
    categories = Category.objects.all()
    return render(request, 'news/index.html', {'categories': categories})

def category_news(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'news/category_news.html', {'category': category})

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_detail.html', {'news': news})
