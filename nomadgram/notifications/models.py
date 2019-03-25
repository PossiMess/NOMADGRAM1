from django.db import models
from nomadgram.users import models as user_models
from nomadgram.images import models as image_models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        

class Notification(TimeStampedModel):
    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    )
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='creator')
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    to = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='to')
    image = models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'from: {}  to: {}'.format(self.creator, self.to)