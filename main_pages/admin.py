from django.contrib import admin
from .models import *




class OperationAdmin(admin.ModelAdmin):
    search_fields = ("title_en",)
admin.site.register(Operation, OperationAdmin)





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





admin.site.site_header = "EHO Administration"
admin.site.site_title = "EHO Site Admin"