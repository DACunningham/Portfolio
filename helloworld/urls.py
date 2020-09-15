from django.urls import path
from django.conf.urls.static import static
from helloworld import views

urlpatterns = [
    path("", views.HomePageView.as_view()),
]
