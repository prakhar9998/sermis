from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from forum.models import Forum
from .serializers import ForumSerializer

class ForumListView(ListAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer