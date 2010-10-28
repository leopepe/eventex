from django import forms
from subscription.models import Subscription

"""
    Import Subscription class
    Inherit forms.ModelForm to transform the objects in html fields

    instanciates Subscription objects into 'model'
    excludes the 'created_at' field
"""

class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        exclude = ('created_at',)
