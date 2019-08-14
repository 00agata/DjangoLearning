from django.contrib import admin
from .models import Person
from .models import Post
from .models import Comment

# Register your models here.
admin.site.register(Person)
#admin.site.register(Post)
admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)