from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Singer)
admin.site.register(Comment)