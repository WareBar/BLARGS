from django.contrib import admin
from .models import Post



# register the Post model into admin panel
admin.site.register(Post)