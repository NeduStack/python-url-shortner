from django.shortcuts import get_object_or_404, render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html' )

def create(request):
    if request.method == 'POST':
        link = request.POST["link"]
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(request, pk):
    #url_details = Url.objects.get(uuid=pk)
    url_details = get_object_or_404(Url, uuid=pk)
    return redirect(''+url_details.link)
