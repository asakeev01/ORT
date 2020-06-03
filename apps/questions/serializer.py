from rest_framework import serializers

from .models import *

class IntroductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Introduction
        fields = ('number', 'name', 'description')
