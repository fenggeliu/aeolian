from django.http import HttpResponse


def index(request):
    return HttpResponse("<h5>Library goes here</h5>")
