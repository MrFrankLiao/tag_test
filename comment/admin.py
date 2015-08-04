# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from comment.models import Comment


# def _comment_tags(obj):
#     if obj.tags:
#         tag_names = ""
#         for name in obj.tags.all():
#             tag_names = name.name + ", " +tag_names
#         return tag_names
#     else:
#         return ""
#
# _comment_tags.allow_tags = True
# _comment_tags.short_description = '標籤'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('msg', 'user')

admin.site.register(Comment, CommentAdmin)

