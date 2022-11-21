from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from global_functions.redirect import reverse_lazy_plus



def svg_viewer(request):
    context = {

    }

    return render(request, 'svg_viewer/svg_viewer.html', context)