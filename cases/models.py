from django.contrib.postgres.indexes import GinIndex
from django.db import models
from fields import MaxCharField

class Case(models.Model):
    title = MaxCharField("Title")
    image = models.ImageField(verbose_name="Image")

    class Meta:
        app_label = 'cases'
        indexes = [
            GinIndex(fields=['title'])
        ]

    def __str__(self):
        return self.title

    def get_stages(self):
        return self.stage_set.all()

    @classmethod
    def search(cls, query):
        return cls.objects.filter(title__search=query)


class Stage(models.Model):
    case = models.ForeignKey("cases.Case", verbose_name="Case")
    title = MaxCharField("Title")
    body = models.TextField()
    step_number = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'cases'
        unique_together = ('case', 'step_number')

    def __str__(self):
        return self.title
