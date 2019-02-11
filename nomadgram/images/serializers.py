from rest_framework import serializers
from nomadgram.users import models as user_models
from . import models

class FeedUserSerializers(serializers.ModelSerializer):

    class Meta:

        model = user_models.User

        fields = (
            'username',
            'profile_image',
        )


class CommentSerializers(serializers.ModelSerializer):
    
    creator = FeedUserSerializers()

    class Meta:
        model = models.Comment
        fields = (
            "id",
            "message",
            "creator",
        )

class LikeSerializers(serializers.ModelSerializer):

    


    class Meta:
        model = models.Like
        fields = '__all__'





class ImageSerializers(serializers.ModelSerializer):

    comments = CommentSerializers(many=True)
    creator = FeedUserSerializers()

    class Meta:
        model = models.Image
        fields = (
        "id",
        "file" ,
        "location" ,
        "caption" ,
        "comments",
        "like_count",
        "creator",
        )