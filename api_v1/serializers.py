from rest_framework import serializers

from cases.models import Case, Stage


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        exclude = ['case']


class CaseSerializer(serializers.ModelSerializer):
    stages = serializers.ListField(child=StageSerializer(), source='get_stages')

    class Meta:
        model = Case
        fields = ['id', 'title', 'stages']