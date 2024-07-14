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
        return render(request, 'index.html')
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError



def about_us_view(request):
    return render(request, 'about.html')
    
    

def csr_view(request):
    try:

        all_csr = CSR.objects.all().order_by("date")
        paginator = Paginator(all_csr, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj":page_obj
        }

        return render(request, 'csr.html', context)
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError




def csr_details(request, id):
    try:

        current_csr = CSR.objects.get(id=id)
        csr_image = CSRImage.objects.filter(related_CSR = current_csr)

        context = {
            "data": current_csr,
            "images": csr_image
        }

        return render(request, 'csr_details.html', context)
    
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError




def management_view(request):
    try:

        all_managers = Manager.objects.all().order_by('start_year')
        context = {
            "managers": all_managers
        }
        return render(request, "management.html", context)
    except Exception as e:
        logger.exception(e)
        return HttpResponseServerError
