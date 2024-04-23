from django.contrib import admin
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    fieldsets = (
        ('', {
            'fields': ('category', 'slug'),
        }),
    )

admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(Category, CategoryAdmin)
