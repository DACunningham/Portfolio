from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def index(request, *args, **kwargs):
    qs = Article.objects.all()
    return render(request, "blog/index.html", context={"articles": qs})


def detail(request, pk, *args, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "blog/detail.html", context={"article": article})