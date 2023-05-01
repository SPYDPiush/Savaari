from django.shortcuts import render,HttpResponse
from .services import UserAtomicService

from extra import MyLogger
logger=MyLogger(__name__).get_logger()

# Create your views here.
def sign_up(request):
    if request.method=="POST":
        form_data=request.POST.copy()
        user=UserAtomicService.create_user(form_data)
        return HttpResponse(user)
    else:
        return HttpResponse('hi')