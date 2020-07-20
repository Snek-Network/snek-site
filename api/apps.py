from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        """Run when the app has been loaded and is ready to serve requests."""
        import api.signals  # NOQA: F401
