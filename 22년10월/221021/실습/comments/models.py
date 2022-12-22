from django.db import models
from reviews.models import Review
from accounts.models import User

# Create your models here.


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
