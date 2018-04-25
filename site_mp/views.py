from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Thing, Message
from .forms import ThingForm
from .forms import ContactForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .token import link_token


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
            current_site = get_current_site(request)
            message = render_to_string('link_email.html', {
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(thing.pk)).decode(),
                'token':link_token.make_token(thing),
            })
            email = EmailMessage(
              'Congratulations !',
              message,
              '#### <noreply@####.fr>',
              '',)
            email.send()
            return redirect('thing_detail', pk=thing.pk)
    else:
        form = ThingForm()
    return render(request, 'site_mp/thing_new.html', {'form': form})

def thing_edit(request, uidb64, token):

    token = request.GET.get('token')
    uidb64 = request.GET.get('uidb64')

    if  uidb64 is not None and token is not None:
        uid = force_text(urlsafe_base64_decode(uidb64))
        try:
            thing_model = get_thing_model()
            thing = thing.objects.get(pk=uid)
            if default_token_generator.check_token(thing, token):
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
        except:
             pass

def contact_author(request, pk):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            thing=get_object_or_404(Thing, pk=pk)
            mess = render_to_string('info_message.html', {'text': message.text, 'email': message.email_user,})
            to_email = form.cleaned_data.get('thing.email_author')
            msg = EmailMessage('Somebody is interested in your thing !', mess, '#### <noreply@####.fr>', '',)
            msg.content_subtype = "html"
            msg.send()
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'site_mp/message_contact.html', {'form': form}) 
 
def delete_thing(request, pk): 
    thing = Thing.objects.get(pk).delete 
    return redirect('/')

