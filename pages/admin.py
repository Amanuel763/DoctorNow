from django.contrib import admin
from .models import Doctor
from django.utils.html import format_html

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'occupation', 'created_date')
    list_display_links = ('id', 'first_name',)
    search_fields = ('first_name', 'last_name', 'occupation',)
    list_filter = ('occupation',)
admin.site.register(Doctor, DoctorAdmin)