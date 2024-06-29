from django.shortcuts import render, redirect
from media_center.models import Event, EventVideo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def handle_404(request, exception):
    print("here")
    return render(request, 'messages/404.html')



def success(request):
    return render(request, 'messages/success.html')


