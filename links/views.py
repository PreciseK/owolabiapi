from django.shortcuts import render
from django.urls import *
from django.views.generic import *
from rest_framework import generícs
from .serizliers import LinkSerializer
from .models import Link
# Create your views here.


class PostListApi(ListApiView):
    queryset = Link.object.filter(active =True)
    serializer_class = LinkSerializer


class PostDetailView(RetrieveApiView):
    queryset = Link.object.filter(active =True)
    serializer_class = LinkSerializer


class PostUpdateApi(UpdateApiView):
    queryset = Link.object.filter(active =True)
    serializer_class = LinkSerializer


class PostDeleteView(DestroyApiView):
    queryset = Link.object.filter(active =True)
    serializer_class = LinkSerializer

