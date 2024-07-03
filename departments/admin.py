from django.contrib import admin
from .models import *




class ICTAdmin(admin.ModelAdmin):
    search_fields = ("title_en",)
admin.site.register(ICT, ICTAdmin)

class DrillingAdmin(admin.ModelAdmin):
    search_fields = ("title_en",)
admin.site.register(Drilling, DrillingAdmin)

class DrillingPetroAdmin(admin.ModelAdmin):
    search_fields = ("title_en",)
admin.site.register(PetroleumEngineering, DrillingPetroAdmin)


class ExplorationAdmin(admin.ModelAdmin):
    search_fields = ("title_en",)
admin.site.register(Exploration, ExplorationAdmin)


class QHSEMainContentAdmin(admin.ModelAdmin):
    search_fields = ("title_en",)
admin.site.register(QHSEMainContent,QHSEMainContentAdmin)



class QHSEContentAdmin(admin.ModelAdmin):
    search_fields = ("content_en",)
admin.site.register(QHSEContent,QHSEContentAdmin)



class QHSEPDFAdmin(admin.ModelAdmin):
    search_fields = ("title",)
admin.site.register(QHSEPDF, QHSEPDFAdmin)

class QHSEVideoAdmin(admin.ModelAdmin):
    search_fields = ("title",)
admin.site.register(QHSEVideo, QHSEVideoAdmin)

class QHSEImageAdmin(admin.ModelAdmin):
    search_fields = ("title",)
admin.site.register(QHSEImage, QHSEImageAdmin)