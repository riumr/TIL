from django.forms import ModelForm
from .models import Review, Comment


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class CommnetForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ("review",)
