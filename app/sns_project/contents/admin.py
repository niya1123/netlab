from django.contrib import admin
from .models import Tag, Contents, Review
# Register your models here.

class ContentsAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_display = ['title', 'is_public', 'updated_at', 'created_at', 'title_len']
    list_filter = ['is_public', 'tags']
    ordering = ('-updated_at',)

    def title_len(self, obj):
        return len(obj.title)

    title_len.short_description = 'タイトルの文字数'

admin.site.register(Contents, ContentsAdmin)
admin.site.register(Tag)
admin.site.register(Review)
