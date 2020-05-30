from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login
from .forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def logout_views(request):
    logout(request)
    return HttpResponseRedirect(reverse('DormitoryManagement:index'))


def register(request):
    context = RequestContext(request)

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password((user.password))
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.prof_pic = request.Files['picture']
            profile.save()

            login(request, user)
            return HttpResponseRedirect(reverse('DormitoryManagement:index'))
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)

def single_post(request):
    return render(request, 'users/gallery-single-post.html')

@login_required
def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk)
    else:
        user = request.user
    args = {'user': user}

    return render(request, 'users/profile.html', args)
