from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers


class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        images= serializers.ImageSerializers(all_images, many=True)

        return Response(data=images.data)

