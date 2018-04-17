from django.shortcuts import render
from django.utils import timezone
from .models import Thing

def thing_list(request):
    things= Thing.objects.order_by('edit_date')
    return render(request, 'site_mp/thing_list.html', {
	'things': things})
