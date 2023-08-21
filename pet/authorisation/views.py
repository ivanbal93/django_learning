from django.shortcuts import render

# Create your views here.


def authorisation(request):
    return render(request, template_name='authorisation.html')
