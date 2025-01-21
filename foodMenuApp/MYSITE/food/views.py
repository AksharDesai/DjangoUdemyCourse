from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

# Create your views here.
# def items(request):
#     item_list = Item.objects.all()
#     context={}
#     context["item_list"]=item_list
    
#     return render(request,'index.html',context)


class itemsCBV(ListView):
    model = Item
    template_name = "index.html"
    context_object_name = 'item_list'

    



def item_detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item':item
    }
    if request.method == "POST":
        item.delete()
        return redirect("/")
    
    return render(request,'detail.html',context)





def item_create(request):
    context={}
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        form.save()
        
    
    
    context["form"]=form
    
    return render(request,'create.html',context)

class CreateItem(CreateView):
    model = Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name='create.html'
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    


def item_update(request,item_id):
    item = Item.objects.get(pk= item_id)

    context={}
    form = ItemForm(instance = item)
    
    if request.method == "POST":
        form = ItemForm(request.POST,instance=item)
        form.save()
   
    
    
    
    context["form"]=form
    context["item"]=item
    return render(request,'update.html',context)