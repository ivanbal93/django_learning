from django.shortcuts import render


# def oauth(request):
#     return render(request, template_name='oauth.html')

def main_page(request):
    return render(request, template_name='default.html')
