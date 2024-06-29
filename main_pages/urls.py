from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us_view, name='about'),
    path('operations-services', views.operation_view, name='operation'),
    path('hse', views.hse_view, name='_hse')

]