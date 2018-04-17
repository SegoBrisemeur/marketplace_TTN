from django.shortcuts import render

def thing_list(request):
    return render(request, 'site_mp/thing_list.html', {})
