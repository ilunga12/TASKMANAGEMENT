from django.contrib import admin

from newapp import models

# Register your models here.
admin.site.register(models.task),
admin.site.register(models.details),