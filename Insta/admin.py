from django.contrib import admin
from Insta.models import Post
from Insta.models import InstaUser, Comment, Like, UserConnection
# Register your models here.

admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserConnection)