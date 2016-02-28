from django.contrib import admin
from myblog.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ('title', 'author', 'created_date', 'modified_date')
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = "{} posts were".format(rows_updated)
        self.message_user(request, "{} successfully marked as published.".format(message_bit))
    make_published.short_description = "Mark selected posts as published."


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

