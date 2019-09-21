from django.contrib import admin
from . models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'text', 'create_date', 'update_date', 'status']
    list_filter = ['status']
    search_fields = ['author']
    fields = ['author', 'email', 'text', 'status']
    list_display_links = ['id', 'author', 'email', 'text']


admin.site.register(Entry, EntryAdmin)
