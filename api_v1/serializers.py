from rest_framework import serializers

from cases.models import Case, Stage
from users.models import User


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        exclude = ['case']


class CaseSerializer(serializers.ModelSerializer):
    stages = serializers.ListField(child=StageSerializer(), source='get_stages')
    image = serializers.ImageField()

    class Meta:
        model = Case
        fields = ['id', 'title', 'stages', 'image', 'description']


class UserSerializer(serializers.ModelSerializer):
    cases = serializers.ListField(child=serializers.DictField() ,source='get_cases')

    class Meta:
        model = User
        fields = ['username', 'cases']
