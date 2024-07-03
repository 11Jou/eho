from django.urls import path
from . import views

urlpatterns = [
    path('hse', views.hse_view, name='_hse'),
    path('exploration', views.exploration_View, name='_exploration'),
    path('operations', views.operation_View, name='_operation'),
    path('ict', views.ict_view, name='_ict'),
]