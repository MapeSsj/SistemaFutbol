from django.shortcuts import render
from django.http import HttpResponse
from .models import competicion
# Create your views here.
from .models import competicion
import json

def obtener_competiciones(request):
    competiciones = list(competicion.objects.all().values('id', 'nombre'))
    data = json.dumps(competiciones)
    return HttpResponse(data, content_type='application/json')