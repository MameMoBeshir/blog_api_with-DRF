from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
# Create your views here.
class PostList(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer