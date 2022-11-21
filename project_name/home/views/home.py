from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from global_functions.redirect import reverse_lazy_plus


def home(request):
  context = {

  }

  return render(request, 'home/home.html', context)