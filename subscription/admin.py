from django.contrib import admin
from eventex.subscription.models import Subscription

class SubscriptionADmin(admin.ModelAdmin):
    fields = ['nome', 'cpf', 'email', 'telefone']
    list_display = ['nome', 'cpf', 'email', 'telefone', 'inscrito_hoje']

#admin site.register(Subscription, SubsciptionAdmin)
