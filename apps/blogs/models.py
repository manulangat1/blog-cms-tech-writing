from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampedUUIDModel

# Create your models here.


User = get_user_model()


class Tag(TimeStampedUUIDModel):
    title = models.CharField(max_length=199)

    def __str__(self) -> str:
        return self.title


class Post(TimeStampedUUIDModel):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=199)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    isPublished = models.BooleanField(default=False)
    image = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.title
