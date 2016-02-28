from django.contrib import admin
from myblog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
admin.site.register(Category, CategoryAdmin)
