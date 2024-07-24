from django.contrib import admin
from .models import *
from .forms import *




class ICTAdmin(admin.ModelAdmin):
    form = ICTForm
    search_fields = ("title_en",)

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.0.min.js',"js/progress_bar.js")

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
    form = QHSEVideoForm
    search_fields = ("title",)

    class Media:
        js = ('https://code.jquery.com/jquery-3.6.0.min.js',"js/progress_bar.js")
        
admin.site.register(QHSEVideo, QHSEVideoAdmin)

class QHSEImageAdmin(admin.ModelAdmin):
    search_fields = ("title",)
admin.site.register(QHSEImage, QHSEImageAdmin)