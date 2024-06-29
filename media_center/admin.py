from django.contrib import admin
from .models import *
from project.export import export_as_csv

# Register your models here.

# myapp/admin.py


class NewsAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("date",)
    actions = [export_as_csv]


class EventAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("date",)
    actions = [export_as_csv]


class CSRAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("date",)
    actions = [export_as_csv]



class CareerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    actions = [export_as_csv]


class ContactAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    actions = [export_as_csv]


admin.site.register(New, NewsAdmin)
admin.site.register(NewsImage)
admin.site.register(Event, EventAdmin)
admin.site.register(EventVideo)
admin.site.register(CSR, CSRAdmin)
admin.site.register(CSRImage)


admin.site.register(Departement)
admin.site.register(Career, CareerAdmin)
admin.site.register(Contact, ContactAdmin)

