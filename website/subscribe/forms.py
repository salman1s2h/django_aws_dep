
from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribs

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribs
        fields='__all__'
        # exclude=('first_name',)
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email')
        }
        help_texts={'first_name':_('Enter characters only')}
        error_messages={
            'first_name':{
                'required':_('You cannot move forward without first name')
            }
        }

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        # Add your custom validation logic
        if len(data) < 5:
            self.add_error('first_name', 'Your field must be at least 5 characters long.')
        elif ';' in data:
            self.add_error('first_name', 'It only consider character')
        return data



