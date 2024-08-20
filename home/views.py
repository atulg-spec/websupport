from django.shortcuts import render
from django.contrib import messages
import csv
from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from django.utils.text import slugify
from .forms import UploadCSVForm
from .models import *

def index(request):
    # media = MediaContent.objects.all()
    context = {
        # "media":media,
    }
    return render(request,'home/tempindex.html',context)



def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            for row in reader:
                title = row['H1Content']
                image_url = row['ThumbnailURL']
                short_video_url = row['VideoURL']
                
                MediaContent.objects.get_or_create(
                    title=title,
                    defaults={
                        'image_url': image_url,
                        'short_video_url': short_video_url,
                        'video_url': short_video_url,  # Assuming no video_url in CSV, set to empty string or modify as needed
                        'slug': slugify(title)
                    }
                )
            return redirect('/')  # Redirect to a success page or another view
    else:
        form = UploadCSVForm()
    return render(request, 'upload_csv.html', {'form': form})

def watch(request, slug):
    post = get_object_or_404(MediaContent, slug=slug)
    media = MediaContent.objects.all()
    context = {
        'post': post,
        'media': media
        }
    return render(request, 'home/watch.html', context)

def privacypolicy(request):
    return render(request,'home/privacypolicy.html')

def refundpolicy(request):
    return render(request,'home/refundpolicy.html')

def about(request):
    return render(request,'home/about.html')

def disclaimer(request):
    return render(request,'home/disclaimer.html')

def termsofuse(request):
    return render(request,'home/termsofuse.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)
