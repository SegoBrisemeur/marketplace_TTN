from django.shortcuts import render
from django.utils import timezone
from .models import Thing
from django.shortcuts import render, get_object_or_404


def thing_list(request):
    things= Thing.objects.order_by('edit_date')
    return render(request, 'site_mp/thing_list.html', {
	'things': things})

def thing_detail(request, pk):
    thing = get_object_or_404(Thing, pk=pk)
    return render(request, 'site_mp/thing_detail.html', {'thing': thing})
