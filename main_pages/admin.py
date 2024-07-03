from django.contrib import admin
from .models import *
from project.export import export_as_csv


class ManagerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("start_year",)
    actions = [export_as_csv]
admin.site.register(Manager, ManagerAdmin)

class CSRAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("date",)
    actions = [export_as_csv]
admin.site.register(CSR, CSRAdmin)


admin.site.register(CSRImage)



admin.site.site_header = "EHO Administration"
admin.site.site_title = "EHO Site Admin"