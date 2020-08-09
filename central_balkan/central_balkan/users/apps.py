from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = "central_balkan.users"
    verbose_name = "Потребители"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
