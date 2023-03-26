from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Author, Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'tags', 'date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
>>>>>>> 0eb7a81 (Blog Website Up and Running)
