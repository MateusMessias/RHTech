from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem indo ao RHTech.")