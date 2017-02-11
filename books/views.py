from django.shortcuts import render
from django.db.models import Q
from .models import Book
# Create your views here.

def search(request):
    query = request.GET.get('q')
    if query:
        qset = (
            Q(title_icontains=query)|
            Q(authors_first_name=query)|
            Q(authors_last_name =query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render("search.html",{"results":results,"query":query})