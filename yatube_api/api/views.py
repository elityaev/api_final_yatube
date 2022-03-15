from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer)
from posts.models import Post, Follow, Group


class MyApiViewSet(viewsets.ModelViewSet):

    def get_prefix(self):
        class_name = self.__class__.__name__
        prefix = class_name[:-7]
        return prefix

    def get_queryset(self):
        prefix = self.get_prefix()
        model = globals().get(prefix)
        queryset = model.objects.all()
        return queryset

    def get_serializer_class(self):
        prefix = self.get_prefix()
        serializer_name = prefix + 'Serializer'
        serializer_class = globals().get(serializer_name)
        return serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(MyApiViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination


class GroupViewSet(MyApiViewSet):
    http_method_names = ['get', 'head']


class CommentViewSet(MyApiViewSet):
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs.get('post_id')
        )


class FollowViewSet(MyApiViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        queryset = Follow.objects.filter(
            user=self.request.user
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user)
