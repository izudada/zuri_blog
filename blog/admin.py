from django.contrib import admin

from .models import Post, Comment

admin.site.site_header = "Blog Admin"

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['title']}),
    ('Author', {'fields' : ['author'], 'classes' : ['collapse']}),
    ('Body', {'fields' : ['body'], 'classes' : ['collapse']}),]

    inlines = [CommentInline]

# admin.site.register(Post)
admin.site.register(Post, QuestionAdmin)

