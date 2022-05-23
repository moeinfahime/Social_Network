from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated')
    # search_fields = ('slug',) #    , indicated that is tuple and important
    search_fields = ('slug', 'body')  # , indicated that is tuple and important
    list_filter = ('updated',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)


# admin.site.register(Post, PostAdmin)  # this line applied for register model or @admin.register(Post) above of class PostAdmin
