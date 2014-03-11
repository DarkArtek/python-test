from django.shortcuts import render
from django.http import HttpResponse
from enrloment.models import EnrModel
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
