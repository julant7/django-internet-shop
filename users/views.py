from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistration


# def login(request):
#     if request.method == 'POST':
#         form = UserOurRegistration(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data('username')
#             return redirect('home')
#     else:
#         form = UserOurRegistration()
#     return render(request, 'users/registration.html', {'form': form})
#

def register(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            return redirect('home')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form})


def password_reset_request(request):
    context = {

    }
    return render(request, 'registration/password_reset_form.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
