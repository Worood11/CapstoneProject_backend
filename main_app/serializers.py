from rest_framework import serializers
from django.db.models import Avg
from .models import Bookstore , Review  , Event
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(source='profile.role', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')

    def validate_password(self, value):
        try:
            validate_password(value) 
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')

        validate_password(password)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password
        )
        return user

class BookstoreSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Bookstore
        fields = ['id', 'name', 'description', 'city', 'image', 'avg_rating']

    def get_avg_rating(self, obj):
        avg = Review.objects.filter(bookstore=obj).aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else None
    
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'title', 'rating', 'body', 'created_at', 'username', 'bookstore' , 'user']
        read_only_fields = ['username', 'bookstore']
   

class EventSerializer(serializers.ModelSerializer):
    bookstore_name = serializers.CharField(source='bookstore.name', read_only=True)
    class Meta:
        model = Event
        fields = fields = ['id', 'name', 'description', 'date', 'time', 'bookstore', 'bookstore_name']