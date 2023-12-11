from django.shortcuts import render, redirect
from . models import Profile


from django.contrib.auth.models import User


from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from . forms import CustomUserCreationForm, ProfileForm, DeviceForm
# Create your views here.

def loginUser(request):
    page= 'login'

    if request.user.is_authenticated:
        return redirect('photographers')


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist....')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('photographers')
        else:
            messages.error(request, "invalid credantials...")

    return render(request, 'photographers/login_registrations.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'user is successfully logged out')
    return redirect('login')



def registerUser(request):
    page = 'registration'
    form = CustomUserCreationForm()


    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'accout has been created successfully...')

            login(request, user)
            return redirect("update")
        
        else:
            messages.error(request, "an error has been occured during registration...")

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'photographers/login_registrations.html', context)




@login_required(login_url='login')
def photographers(request):

    photographers = Profile.objects.all()
    messages.success(request, 'user is successfully logged in')

    context = {
        'photographers': photographers,
    }
    return render(request, 'photographers/photographers.html', context)



def photographer(request, pk):

    photographer = Profile.objects.get(id=pk)

    context = {
        'photographer': photographer,
    }
    return render(request, 'photographers/photographer.html', context)


@login_required(login_url="login")
def createAccount(request):
    photographer = request.user.profile

    context = {
        'photographer': photographer,
    }
    return render(request, 'photographers/account.html', context)


@login_required(login_url='login')
def updateAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
        
    context = {
        'form':form,
    }
    return render(request, 'photographers/updateAccount.html', context)

@login_required(login_url='login')
def createDevice(request):
    profile = request.user.profile
    form = DeviceForm()

    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.owner = profile
            device.save()
            return redirect("photos")


    context = {
        'form':form,
    }
    return render(request, "photographers/device.html", context)


@login_required(login_url='login')
def updateDevice(request, pk):
    profile = request.user.profile
    device = profile.device_set.get(id=pk)
    form = DeviceForm(instance=profile)

    if request.method == "POST":
        form = DeviceForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("photos")


    context = {
        'form':form,
    }
    return render(request, "photographers/updateDevice.html", context)