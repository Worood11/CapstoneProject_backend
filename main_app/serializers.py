from rest_framework import serializers
from .models import Bookstore , Review  , Event
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # Add a password field, make it write-only
    # prevents allowing 'read' capabilities (returning the password via api response)
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
      
        return user

class BookstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookstore
        fields = '__all__'
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    bookstore_name = serializers.CharField(source='bookstore.name', read_only=True)
    class Meta:
        model = Event
        fields = fields = ['id', 'name', 'description', 'date', 'time', 'bookstore', 'bookstore_name']