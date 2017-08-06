from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    
    a=1
    #html = "<html><body>It is now %s.</body></html>" % now
    
    return render(request,"monitor.html",locals()) 
