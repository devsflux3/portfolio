from django.shortcuts import render

# Create your views here.


def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '404.html', status=500)

def error_403(request, exception):
    return render(request, '404.html', status=403)

def error_400(request, exception):
    return render(request, '404.html', status=400)

def index(request):
    template_name = "master_app/index.html"
    context = {
    
    }
    return render(request, template_name, context)
