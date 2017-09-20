from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cases = models.ManyToManyField("cases.Case", verbose_name="Cases")
    avatar = models.ImageField(
        verbose_name='Avatar',
        upload_to='userpics',
        blank=True,
    )

    class Meta:
        app_label = 'users'
