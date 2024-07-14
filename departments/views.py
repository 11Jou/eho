from django.shortcuts import render
from django.http import HttpResponseServerError
from django.core.paginator import Paginator
from .models import *
import logging



logger = logging.getLogger(__name__)


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



def exploration_View(request):
    try:

        all_exploration = Exploration.objects.all()
        context = {
            'explorations': all_exploration
        }
        return render(request, "exploration.html", context)
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError


def operation_View(request):
    try:

        all_drilling = Drilling.objects.all()
        all_drilling_petro = PetroleumEngineering.objects.all()

        context = {
            'drilling': all_drilling,
            'petro': all_drilling_petro
        }
        return render(request, "drilling.html", context)
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError



def ict_view(request):
    try:

        all_blogs = ICT.objects.all()
        context = {
            "blogs": all_blogs
        }
        return render(request, "ict.html", context)
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError