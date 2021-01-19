from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']