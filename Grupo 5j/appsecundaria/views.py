from django.shortcuts import render

# Create your views here.

def Index_vista(request):
    return render(request,"index.html")