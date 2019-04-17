from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request,*args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello, World</h1>")
    my_context = {

        "my_text"   : "This is about us",
        "my_number" : 123,
        "my_list"   : [123,1231,1231231]

    }
    return render(request, "home.html",my_context)

def contact_view(*args,**kwargs):
    return HttpResponse("<h1>Contacts</h1>")

def product_view(*args,**kwargs):
    return HttpResponse("<h1>Products</h1>")