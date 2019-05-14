from .views import ForumListView
from django.urls import path

urlpatterns = [
    path('', ForumListView.as_view()),
]