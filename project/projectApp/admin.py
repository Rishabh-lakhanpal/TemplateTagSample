from django.contrib import admin
from .models import YourModel
# Register your models here.

@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')