from django.contrib import admin

from .models import About, home, post
# Register your models here.



admin.site.register(home)
admin.site.register(About)
admin.site.register(post)