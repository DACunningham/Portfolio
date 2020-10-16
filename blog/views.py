from django.views.generic import ListView, DetailView
from .models import Article


class ArticleList(ListView):
    model = Article
    template_name = "blog/index.html"


class ArticleDetail(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = "article"
