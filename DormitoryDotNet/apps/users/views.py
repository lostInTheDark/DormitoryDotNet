from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import revers
from django.contrib.auth import logout

def logout_views(request):
    logout(request)
    return HttpResponseRedirect(reverse('DormitoryManagement:index'))

