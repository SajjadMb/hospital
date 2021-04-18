from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from .signals import create_user_profile , save_profile



class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = _('accounts')

    def ready(self):
        import accounts.signals
