from django.db import models
from fields import MaxCharField

class Case(models.Model):
    title = MaxCharField("Title")

    class Meta:
        app_label = 'cases'

    def __str__(self):
        return self.title

    def get_stages(self):
        return self.stage_set.all()

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
