from django.urls import path
from . import views

urlpatterns = [
    path('forums/', views.forum_list, name='forums'),
]