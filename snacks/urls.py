from django.urls import path  # 1. import any thing built in django
from .views import HomePage,SnackListView, SnackDetailView  # 2. import from yout application

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('snacks', SnackListView.as_view(),name="snacks"),
    path('snacksdetail', SnackDetailView.as_view(),name="snacksdetail")
]