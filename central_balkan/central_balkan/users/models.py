from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse


class User(AbstractUser):
    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администратори'

    name = CharField("Име", blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
