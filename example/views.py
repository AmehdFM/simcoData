# example/views.py
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import os
from supabase import create_client, Client
from django.http import JsonResponse

def index(request):
  return render(request, 'index.html')