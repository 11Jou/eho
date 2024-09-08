from django.shortcuts import render
from django.http import HttpResponseServerError
from django.core.paginator import Paginator
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ICTForm
import logging




logger = logging.getLogger(__name__)

#HSE
def hse_view(request):
    try:
        objects = QHSEMainContent.objects.all()
        new_dict = {}
        for object in objects:
            lines = QHSEContent.objects.filter(related_title = object)
            new_dict[object] = lines

        context = {
            "policy":new_dict,
        }
        print(context)
        return render(request, "HSE.html", context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError
 
 
    
def hse_pdf(request):
    try:
        pdfs = QHSEPDF.objects.all()
        context = {
            "pdfs":pdfs,
        }
        return render(request, "hse_pdf.html", context)  
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError



def hse_photo(request):
    try:
        page_number = request.GET.get('page')
        images = QHSEImage.objects.all()
        paginator_images = Paginator(images, 30)
        page_obj_images = paginator_images.get_page(page_number)
        context = {
            "page_obj_images":page_obj_images,
        }
        return render(request, "hse_photo.html", context)  
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError


def hse_video(request):
    try:
        page_number = request.GET.get('page')
        videos = QHSEVideo.objects.all()
        paginator_videos = Paginator(videos, 30)
        page_obj_videos = paginator_videos.get_page(page_number)
        context = {
            "page_obj_videos": page_obj_videos
        }
        return render(request, "hse_video.html", context)  
        
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError
    
#Exploration 
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



#Operation
def operation_View(request):
    try:

        all_drilling = Drilling.objects.all()

        context = {
            'drilling': all_drilling,
        }
        return render(request, "drilling.html", context)
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError
    



def operation_petro_view(request):
    try:
        all_drilling_petro = PetroleumEngineering.objects.all()
        context = {
            'petro': all_drilling_petro
        }
        return render(request, "petro.html", context)
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError



#ICT
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
    
