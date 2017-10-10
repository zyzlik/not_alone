from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    stages = models.ManyToManyField("cases.Stage", verbose_name="Stages")
    avatar = models.ImageField(
        verbose_name='Avatar',
        upload_to='userpics',
        blank=True,
    )

    class Meta:
        app_label = 'users'
        indexes = [
            GinIndex(fields=['username'])
        ]

    @property
    def cases(self):
        return [stage.case for stage in self.stages.all()]

    def get_cases(self):
        lst = []
        for stage in self.stages.select_related('case'):
            dct = {}
            dct[stage.case.title] = {}
            dct[stage.case.title]['stage'] = stage.title
            dct[stage.case.title]['step'] = stage.step_number
            lst.append(dct)
        return lst

    @classmethod
    def search(cls, query):
        return cls.objects.filter(username__search=query)
