from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseServerError
from .models import *
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def news_view(request):
    try:    
        all_news = New.objects.all().order_by('date')
        paginator = Paginator(all_news, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj
        }
        return render(request, 'news.html', context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError()




def news_details(request, id):
    try:

        current_new = New.objects.get(id=id)
        news_images = NewsImage.objects.filter(related_news = current_new)
        context = {
            "data" : current_new,
            'images' : news_images
        }
        return render(request, 'news_details.html', context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError()



def events_view(request):
    try:

        all_events = Event.objects.all().order_by('date')
        paginator = Paginator(all_events, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj
        }
        return render(request, 'events.html', context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError()





def events_details(request, id):
    try:

        current_event = Event.objects.get(id=id)
        event_gallery = EventVideo.objects.filter(related_event = current_event)
        context = {
            "data" : current_event,
            'videos' : event_gallery
        }
        return render(request, 'event_details.html', context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError()





def career_view(request):
    all_dept = Departement.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('mail')
        phone = request.POST.get('phone')
        dept = request.POST.get('department')
        resume = request.FILES.get('resume')

        choosen_dept = Departement.objects.get(id=dept)

        new_record = Career(departement = choosen_dept, name = name, email = email, phone_number = phone, resume = resume)
        new_record.save()

        return redirect('_success')

    context = {
        'depts' : all_dept
    }
    return render(request, 'career.html', context)


def contact_us_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('mail')
        message = request.POST.get('msg')

        new_msg = Contact(name = name, email = email, message = message)
        new_msg.save()

        return redirect('_success')
    
    return render(request, 'contact.html')


