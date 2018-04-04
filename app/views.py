from django.shortcuts import render
from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

class ComponycategoryCreateApi(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# @api_view([..])
@permission_classes((permissions.AllowAny,))
class Api(APIView):

    def get(self, request):
        model = Category.objects.all()
        serializers = CategorySerializer(Category, many=True)
        return Response(serializers.data)