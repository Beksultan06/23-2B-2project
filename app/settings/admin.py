from django.contrib import admin
from app.settings.models import Settings
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['id', 'title']
    search_fields = ['id', 'title']