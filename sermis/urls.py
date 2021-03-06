from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('api/', include('forum.api.urls')),
]
