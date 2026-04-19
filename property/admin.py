from django.contrib import admin

from .models import Flat
from .models import Complaint


class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ['liked_by']
    list_display = [
        'address', 
        'price', 
        'new_building', 
        'construction_year', 
        'town'
        ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number']
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ['created_at']

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

