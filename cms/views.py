from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages
# Create your views here.


def show(request):
    resp = "Las direcciones disponibles son: "
    lista_pages = Pages.objects.all()
    for page in lista_pages:
        resp += "<br>-/" + page.name + " --> " + page.page
    return HttpResponse(resp)


def process(request, req):
    try:
        page = Pages.objects.get(name=req)
        resp = "La página solicitada es /" + page.name + " --> " + page.page
    except Pages.DoesNotExist:
        resp = "La página introducida no está en la base de datos"
    return HttpResponse(resp)
