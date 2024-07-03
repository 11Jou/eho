from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us_view, name='about'),
    path('csr', views.csr_view, name='_csr'),
    path('csr/<int:id>', views.csr_details, name='details-csr'),
    path('management', views.management_view, name='_management'),
]