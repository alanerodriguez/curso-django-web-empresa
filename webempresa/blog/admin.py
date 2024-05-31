from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'author', 'published', 'Post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','author__username')
    list_filter = ('author__username','categories__name')

    def Post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    Post_categories.short_description = 'Categorias'


admin.site.register(Post, PostAdmin)