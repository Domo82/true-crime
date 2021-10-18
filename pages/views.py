from django.http import HttpResponse

def indexPageView(request):
    return HttpResponse('Welcome to True Crime')

def contactPageView(request):
    return HttpResponse('Contact us on 087 1234567')
