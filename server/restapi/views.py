from .models import Blogger
from rest_framework import viewsets
from .serializers import BloggerSerializer

class BloggerViewset(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer