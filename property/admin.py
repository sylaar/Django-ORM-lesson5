from django.contrib import admin

from .models import Complaint
from .models import Flat
from .models import Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner', 'flat',]

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
    list_filter = ['new_building', 'rooms_number',]
    search_fields = ('town', 'address', 'owners',)
    readonly_fields = ['created_at']
    inlines = [OwnerInline]

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owners_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

