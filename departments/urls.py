from django.urls import path
from . import views

urlpatterns = [
    path('hse', views.hse_view, name='_hse'),
    path('exploration', views.exploration_View, name='_exploration'),
    path('drilling', views.operation_View, name='_operation'),
    path('petroleum-activities', views.operation_petro_view, name='_operation2'),

    path('ict', views.ict_view, name='_ict'),
    # path('upload/', views.upload_file, name='upload_file'),
]