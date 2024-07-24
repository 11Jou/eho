from django.contrib import admin
from .models import *
from project.export import export_as_csv
from .forms import *

# Register your models here.

# myapp/admin.py


class NewsAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("date",)
    actions = [export_as_csv]

admin.site.register(New, NewsAdmin)


class EventAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("date",)
    actions = [export_as_csv]

admin.site.register(Event, EventAdmin)


class CareerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    actions = [export_as_csv]

admin.site.register(Career, CareerAdmin)


class ContactAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    actions = [export_as_csv]

admin.site.register(Contact, ContactAdmin)


admin.site.register(NewsImage)

class EventVideoAdmin(admin.ModelAdmin):
    form = EventVideoAdminForm
    class Media:
        js = ('https://code.jquery.com/jquery-3.6.0.min.js',"js/progress_bar.js")
        
admin.site.register(EventVideo)


admin.site.register(Departement)

