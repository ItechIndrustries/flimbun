from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(profile)
admin.site.register(message)
admin.site.register(Group)
admin.site.register(fchat)