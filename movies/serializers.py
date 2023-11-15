from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        average_rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if average_rate:
            return round(average_rate, 1)
