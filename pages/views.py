from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

# def password_change_form_view(request, *args, **kwargs):
    # return render(request, "password_change_form.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    my_context = {
        "title": "Welcome to our Social Page",
    }
    return render(request, "social.html", my_context)


def profile_view(request, *args, **kwargs):
    my_context = {
        "title": "Welcome to our Profile Page",
    }
    return render(request, "profile.html", my_context)

def change_view(request, *args, **kwargs):
    my_context = {
        "title": "Welcome to our Profile Page",
    }
    return render(request, "users/password_change_form.html", my_context)