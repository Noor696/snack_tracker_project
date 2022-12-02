from django.urls import path
from .views import HomePage,SnackListView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('snacks', SnackListView.as_view(),name="snacks")
]