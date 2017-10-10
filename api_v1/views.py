import json

from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.views import APIView, Response

from cases.models import Case, Stage
from users.models import User
from .serializers import CaseSerializer, UserSerializer


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CaseSerializer

    def get_queryset(self):
        prefetch = Prefetch('stage_set', queryset=Stage.objects.order_by('step_number'))
        queryset = Case.objects.prefetch_related(prefetch)
        return queryset


class SearchView(APIView):
    TYPES = {
        'cases': (Case, 'title__search', CaseSerializer),
        'users': (User, 'username__search', UserSerializer)
    }

    def get(self, request, format=None):
        query = request.GET.get('q')
        q_type = request.GET.get('type', 'all')
        data = {"result": []}
        if query:
            if q_type != 'all':
                res = self.perform_search(query, q_type)
            else:
                res = self.perform_search(query, 'users') + self.perform_search(query, 'cases')
            data['result'] = res
            resp = Response()
            resp.data = json.dumps(data)
            resp.status = 200
            return resp

    def perform_search(self, query, q_type):
        model, field, serializer = self.TYPES[q_type]
        filter_param = {field: query}
        return serializer(model.objects.filter(**filter_param), many=True).data
