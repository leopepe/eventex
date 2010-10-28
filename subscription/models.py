from django.db import models
from django.utils.translation import ugettext as _


class Subscription(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=15, unique=True, blank=False)
    email = models.EmailField(_('E-mail'), unique=True)
    phone = models.CharField(_('Telefone'), max_length=20, blank=True)
    created_at = models.DateTimeField(_('CriadoEm'), auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (u'Inscricao')
        verbose_name_plural = (u'Inscricoes')
