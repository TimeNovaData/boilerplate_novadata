from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from global_functions.redirect import reverse_lazy_plus



def design_system(request):
    context = {

    }

    return render(request, 'design_system/design_system.html', context)