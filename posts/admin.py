from django.contrib import admin

from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields':(
            'slug',
            'author',
            'likes',
        )}),
        ('Post Informations', {'fields':(
            'title',
            'description',
            'created_date',
        )})
    )

admin.site.register(Comment)