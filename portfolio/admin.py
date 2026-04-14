from django.contrib import admin
from .models import TattooWork


@admin.register(TattooWork)
class TattooWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)


from django.contrib import admin

# Register your models here.
