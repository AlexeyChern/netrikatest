from rest_framework import serializers
from .models import City, People


class Peopler(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id', 'fio', 'city')


class Cityer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'cityname')
