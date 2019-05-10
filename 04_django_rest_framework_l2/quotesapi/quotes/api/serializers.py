from rest_framework import serializers
from quotes.models import Quotes


class QuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quotes
        fields = '__all__'
