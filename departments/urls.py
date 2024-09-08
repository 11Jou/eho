from django.urls import path
from . import views

urlpatterns = [
    path('hse', views.hse_view, name='_hse'),
    path('hse-pdf', views.hse_pdf, name='hse_pdf'),
    path('hse-gallery', views.hse_photo, name='hse_gallery'),
    path('hse-video', views.hse_video, name='hse_video'),

    path('exploration', views.exploration_View, name='_exploration'),
    path('drilling', views.operation_View, name='_operation'),
    path('petroleum-activities', views.operation_petro_view, name='_operation2'),

    path('ict', views.ict_view, name='_ict'),
    # path('upload/', views.upload_file, name='upload_file'),
]