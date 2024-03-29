from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "movie_name", "created_at"]


admin.site.register(Review, ReviewAdmin)
