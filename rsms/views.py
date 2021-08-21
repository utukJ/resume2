from django.http.response import HttpResponseRedirect
from django.urls import reverse
from rsms.models import Contact, ContactForm
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ContactForm()
    
    return render(request, "resume.html", {"form" : form})
    
