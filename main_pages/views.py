from django.shortcuts import render
from .models import *
from django.http import HttpResponseServerError
from django.core.paginator import Paginator
import logging
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    try:

        first_operations = Operation.objects.all()
        paginator = Paginator(first_operations, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "operations": page_obj,
        }

        return render(request, 'index.html', context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError



def about_us_view(request):
    return render(request, 'about.html')
    



def operation_view(request):
    try:
        operations = Operation.objects.all()
        context = {
            "operations": operations
        }

        return render(request, 'operation.html', context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError



def hse_view(request):
    try:
        pdfs = QHSEPDF.objects.all()
        images = QHSEImage.objects.all()
        paginator_images = Paginator(images, 12)
        videos = QHSEVideo.objects.all()
        paginator_videos = Paginator(videos, 12)
        page_number = request.GET.get('page')
        page_obj_images = paginator_images.get_page(page_number)
        page_obj_videos = paginator_videos.get_page(page_number)
        objects = QHSEMainContent.objects.all()
        new_dict = {}
        for object in objects:
            lines = QHSEContent.objects.filter(related_title = object)
            new_dict[object] = lines

        context = {
            "policy":new_dict,
            "pdfs":pdfs,
            "page_obj_images":page_obj_images,
            "page_obj_videos": page_obj_videos
        }


        return render(request, "HSE.html", context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError


