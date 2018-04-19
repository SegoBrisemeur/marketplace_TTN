from django.shortcuts import render
from django.utils import timezone
from .models import Thing
from django.shortcuts import render, get_object_or_404
from .forms import ThingForm
from django.shortcuts import redirect



def thing_list(request):
    things= Thing.objects.order_by('edit_date')
    return render(request, 'site_mp/thing_list.html', {
	'things': things})

def thing_detail(request, pk):
    thing = get_object_or_404(Thing, pk=pk)
    return render(request, 'site_mp/thing_detail.html', {'thing': thing})

def thing_new(request):
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.created_date = timezone.now()
            thing.edit_date = timezone.now()
            thing.save()
            return redirect('thing_detail', pk=thing.pk)
    else:
        form = ThingForm()
    return render(request, 'site_mp/thing_edit.html', {'form': form})

def thing_edit(request, pk):
    thing = get_object_or_404(Thing, pk=pk)
    if request.method == "POST":
        form = ThingForm(request.POST, instance=thing)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.edit_date = timezone.now()
            thing.save()
            return redirect('thing_detail', pk=thing.pk)
    else:
        form = ThingForm(instance=thing)
    return render(request, 'site_mp/thing_edit.html', {'form': form})
