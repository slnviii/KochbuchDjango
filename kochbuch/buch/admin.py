from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Theme)

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inLines = (ProfileInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'created')
