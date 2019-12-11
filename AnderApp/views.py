from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    html_content = "<html><head><title>Olá, Anderson</title></head><body>"
    html_content += "<strong>Olá Anderson</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"

    return HttpResponse(html_content)

# Create your views here.
