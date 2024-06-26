from django.apps import AppConfig


class RequestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reqs'

    def ready(self):
        import reqs.signals
        import reqs.converters
