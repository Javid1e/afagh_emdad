# support_tickets/apps.py
from django.apps import AppConfig


class SupportTicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'support_tickets'

    def ready(self):
        import support_tickets.signals
