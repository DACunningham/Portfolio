from django.urls import path, include
from django.conf.urls.static import static
from site_base import views
from django.conf import settings

urlpatterns = [
    path("", views.HomePageView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
]
