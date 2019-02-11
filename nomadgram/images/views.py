from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        print(following_users)

        image_list = []

        for la in following_users:

            following_images = la.images.all()[:2]

            for image in following_images:

                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializers(sorted_list, many=True)


        return Response(serializer.data)





