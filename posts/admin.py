from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post

# Register your models here.
class CustomPostAdmin(admin.ModelAdmin):
    list_display=("title","author")
    search_fields=("title",)

admin.site.register(Post,CustomPostAdmin)
