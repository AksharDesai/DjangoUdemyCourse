from django.shortcuts import render,redirect
from .models import Movies
import json

from django.http import JsonResponse

from django.core.paginator import Paginator

from .forms import MovieForm

from django.views.decorators.http import require_http_methods

from django.views.decorators.http import require_http_methods

# Create your views here.


def movie_list(request,movie_id=None):
    context={}
    movie_object = Movies.objects.all()#queryset containing all movies (ex:6)
    form = MovieForm()
    

        
        
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie =form.save()
            
            kachraJson = {
                'id':movie.id,
                'name':movie.name,
                'rating':movie.rating,
            }
            
            return JsonResponse(kachraJson)
        
        
    
        

    #search
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name != None:
        movie_object = Movies.objects.filter(name__icontains=movie_name)
    
    
    #pagination
    paginator = Paginator(movie_object,40)#paginator splits 6 movies into 2 pages
    page = request.GET.get('page') #gets current page number
    movie_object = paginator.get_page(page)#returns page 2
    
    
    
    context['movie_object']=movie_object
    context['form']=form

    return render(request,'movie_list.html',context)




def movie_delete(request, movie_id):
    try:
        movie = Movies.objects.get(id=movie_id)
        movie.delete()
        return JsonResponse({'status': 'success'})
    except Movies.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Movie not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)



@require_http_methods(["GET", "PUT"]) 
def movie_update(request, movie_id):
    try:
        movie = Movies.objects.get(id=movie_id)  # Get the movie by ID
    except Movies.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Movie not found'}, status=404)

    if request.method == "PUT":
         try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            form = MovieForm(data, instance=movie)
            if form.is_valid():
                saved_movie = form.save()
                # Return updated movie data
                return JsonResponse({
                    'id': saved_movie.id,
                    'name': saved_movie.name,
                    'rating': saved_movie.rating,
                })
            else:
                # Return form errors
                return JsonResponse(form.errors, status=400)
         except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    else:
        # GET request: Return movie data for editing
        return JsonResponse({
            'id': movie.pk,
            'name': movie.name,
            'rating': movie.rating,
        })