from rest_framework import serializers
from .models import Bookstore

class BookstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookstore
        fields = '__all__'