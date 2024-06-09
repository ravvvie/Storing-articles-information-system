from django.contrib import admin
from .models import (
    Article,
    ArticleScope,
    HistoricalPerson,
    ArticleImage,
)


class ImageAdminInline(admin.TabularInline):
    model = ArticleImage


class HistoricalPersonAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name"]


class ArticleScopeAdmin(admin.ModelAdmin):
    list_display = ["id", "scope"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'description',
        'created_at', 'updated_at', 'get_html_image',
    ]
    inlines = [ImageAdminInline]
    list_filter = ['persons', 'created_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleScope, ArticleScopeAdmin)
admin.site.register(HistoricalPerson, HistoricalPersonAdmin)
