from django.shortcuts import render
from django.http import  HttpResponse
import datetime
# Create your views here.
def current_time(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

def index(request):
    html = '<!DOCTYPE html> <html lang="en"> <head><meta charset="UTF-8"><title>Index</title></head>  <body> Welcome to zjlyyq home! </body> </html> '
    return render(request,'index.html')

def plus_times(request,offset):
    #offset = int(offset)
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = '<html><body>In %s hours,it will be %s.</body></html>' %(offset,dt)
    return HttpResponse(html)
