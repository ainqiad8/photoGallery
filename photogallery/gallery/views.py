from django.shortcuts import render, redirect
from . models import Photos
from . forms import PhotoGraphyForm

from django.contrib.auth.decorators import login_required
# Create your views here.

def photos(request):
    photos = Photos.objects.all()

    context = {
        'photos': photos,
    }
    return render(request, 'gallery/photos.html', context)
    

def photo(request, pk):
    photo = Photos.objects.get(id=pk)
    context = {
        'photo': photo,
    }
    return render(request, 'gallery/photo.html', context)

@login_required(login_url='login')
def create_photo(request):
    profile = request.user.profile
    form = PhotoGraphyForm()

    if request.method == "POST":
        form = PhotoGraphyForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = profile
            form.save()
            return redirect('photos')
    context = {
        'form': form,
    }   
    return render(request, 'gallery/photo_form.html', context)

@login_required(login_url='login')
def update_photo(request, pk):
    profile = request.user.profile
    photos = profile.photos_set.get(id = pk)
    form = PhotoGraphyForm(instance=photos)

    if request.method == "POST":
        form = PhotoGraphyForm(request.POST, request.FILES, instance=photos)
        if form.is_valid():
            form.save()
            return redirect("photos")
    
    context = {
        'form': form,  
    }
    return render(request, 'gallery/update_form.html', context)

@login_required(login_url='login')
def delete_photo(request, pk):
    profile = request.user.profile
    photo = profile.photos_set.get(id=pk)
    
    if request.method == "POST" and request.user.is_authenticated:
        photo.delete()
        return redirect("photos")
    
    context = {
        "photo": photo,
    }
    return render(request, 'gallery/delete_photo.html', context)

