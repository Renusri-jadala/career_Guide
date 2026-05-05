from django.contrib import admin

# Register your models here.
from .models import wish,CareerPath,Technology
admin.site.register(wish)
admin.site.register(CareerPath)
admin.site.register(Technology)