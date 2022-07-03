from django.contrib import admin
from .models import Link
# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('author', 'description', 'targeted_url', 'active')