# from django.shortcuts import render
 
from .models import *
from .serializer import * 
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import filters
# from permission import FullDjangoModelPermissions
# Create your views here. 
class ShopSetView(viewsets.ModelViewSet):
    queryset = shop.objects.all()
    serializer_class = shopSerializer 
class ReviewSetView(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = reviewSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["shop_id",] 