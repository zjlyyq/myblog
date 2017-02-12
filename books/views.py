from django.shortcuts import render
from django.db.models import Q
from .models import Book
# Create your views here.

def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(title__icontains=query)|
            Q(authors__first_name__icontains=query)|
            Q(authors__last_name__icontains=query)                 #中间竟然是两个下划线
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render(request,"search.html",{"results":results,"query":query})