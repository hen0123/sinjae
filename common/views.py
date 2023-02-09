from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth import get_user_model
from .forms import UpdateUserForm, UpdateProfileForm

User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'common/main.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

#마이페이지
def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'common/detail.html', context)

# new 마이페이지
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='/')
            #return redirect(reverse('common/profile'))
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'common/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def secret(request):
    return render(request, 'common/secret.html')