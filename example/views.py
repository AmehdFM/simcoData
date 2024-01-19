# example/views.py
from datetime import datetime

from django.http import HttpResponse

def inde(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def index(request)
    titulo = "hola pe"
    return render(request, 'index.html',{'titulo':titulo})