from django.db.models import Prefetch
from rest_framework import viewsets

from cases.models import Case, Stage
from .serializers import CaseSerializer


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CaseSerializer

    def get_queryset(self):
        prefetch = Prefetch('stage_set', queryset=Stage.objects.order_by('step_number'))
        queryset = Case.objects.prefetch_related(prefetch)
        return queryset
