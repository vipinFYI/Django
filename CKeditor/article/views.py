from nntplib import ArticleInfo
from django.shortcuts import render

# Create your views here.
from .models import Article

def index(request):

    articles = Article.objects.all()
    return render(request, 'article/index.html',{'articles':articles})
