"""stocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include

# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r"users", views.UserViewSet)
# router.register(r"groups", views.GroupViewSet)
# router.register(r"upload", views.MyFileView)

urlpatterns = [
    path("", views.TransactionList.as_view(), name="index"),
    # path("", include(router.urls)),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("upload_api/", views.MyFileView.as_view(), name="file-upload-api"),
    path("upload/", views.upload_file, name="file-upload"),
]
