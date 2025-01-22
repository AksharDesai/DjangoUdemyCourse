from django.shortcuts import render
from .models import Movies

from django.core.paginator import Paginator
# Create your views here.


def movie_list(request):
    context={}
    movie_object = Movies.objects.all()#queryset containing all movies (ex:6)
    
    movie_name = request.GET.get('movie_name')
    
    if movie_name != '' and movie_name != None:
        movie_object = Movies.objects.filter(name__icontains=movie_name)
    
    
    paginator = Paginator(movie_object,4)#paginator splits 6 movies into 2 pages
    page = request.GET.get('page') #gets current page number
    movie_object = paginator.get_page(page)#returns page 2
    context['movie_object']=movie_object
    return render(request,'movie_list.html',context)



