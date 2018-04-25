from django import forms
from .models import Thing, Message

class ThingForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = ('title', 'desc', 'email_author')

class ContactForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('email_user', 'text')
