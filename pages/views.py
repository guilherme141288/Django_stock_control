from django.shortcuts import render

# Create your views here.


def index(request):
    template_html = 'index.html'
    
    return render(request, template_html )