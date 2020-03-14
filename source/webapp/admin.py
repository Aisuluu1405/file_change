from django.contrib import admin
from webapp.models import File, Private


class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'create', 'author']
    list_filter = ['access']
    search_fields = ['name', 'access']
    exclude = []
    readonly_fields = ['create']


admin.site.register(File, FileAdmin)
admin.site.register(Private)

