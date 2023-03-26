from django.contrib import admin
from .models import Book, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'rating')
    list_filter = ('title', 'author', 'rating')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)