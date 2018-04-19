from django.shortcuts import render
from django.utils import timezone
from .models import Thing
from django.shortcuts import render, get_object_or_404
from .forms import ThingForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import link_token
from django.core.mail import EmailMessage


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
	    		message = render_to_string('link_edit.html',{'domain': current_site.domain,'uid':urlsafe_base64_encode(force_bytes(thing.pk)),'token':link_token.make_token(thing),})
	    		to_email = form.cleaned_data.get('email_author')
	    		email = EmailMessage('Link to edit your announce', message, to=[to_email])
	    		email.send()
	    		return redirect('thing_detail', thing.pk)
    	else:
        	form = ThingForm()
    		return render(request, 'site_mp/thing_new.html', {'form': form})

def thing_edit(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
	thing = Thing.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
	thing = None
    if thing is not None and link_token.check_token):
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













