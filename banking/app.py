from django.apps import AppConfig


class BankingAppConfig(AppConfig):
    name = "banking"

    def ready(self):
        from banking import signals # pylint: disable=unused-variable
