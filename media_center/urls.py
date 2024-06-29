from django.urls import path
from . import views

urlpatterns = [
    path('news', views.news_view, name='_news'),
    path('news/<int:id>', views.news_details, name='_details'),


    path('events', views.events_view, name='_events'),
    path('events/<int:id>', views.events_details, name='details-events'),

    
    path('csr', views.csr_view, name='_csr'),
    path('csr/<int:id>', views.csr_details, name='details-csr'),


    path('career', views.career_view, name='_career'),
    path('contact', views.contact_us_view, name='_contact')



]