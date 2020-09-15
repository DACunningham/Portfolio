from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request, *args, **kwargs):
    qs = Article.objects.all()
    return render(request, "blog/index.html", context={"articles": qs})
