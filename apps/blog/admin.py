from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BlogUser)
admin.site.register(Post)
admin.site.register(BlogGroup)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Tag)