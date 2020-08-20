from django.contrib import admin
from .models import Tag, Content, Review, Choice
# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_display = ['title', 'is_public', 'updated_at', 'created_at', 'title_len']
    list_filter = ['is_public', 'tag']
    ordering = ('-updated_at',)

    def title_len(self, obj):
        return len(obj.title)

    title_len.short_description = 'タイトルの文字数'

admin.site.register(Content, ContentAdmin)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Choice)
