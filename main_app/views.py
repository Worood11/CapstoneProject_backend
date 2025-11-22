from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import Bookstore, Review, Event
from .serializers import (
    BookstoreSerializer,
    ReviewSerializer,
    UserSerializer,
    EventSerializer
)
from .permissions import IsReviewOwner, IsAdminUserOrReadOnly

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }
        return Response(data, status=status.HTTP_201_CREATED)


class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class Home(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the API home route!'})



class BookstoresIndex(APIView):
    serializer_class = BookstoreSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request):
        queryset = Bookstore.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookstoreDetail(APIView):
    serializer_class = BookstoreSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, bookstore_id):
        bookstore = get_object_or_404(Bookstore, id=bookstore_id)
        serializer = self.serializer_class(bookstore)
        return Response(serializer.data)

    def put(self, request, bookstore_id):
        bookstore = get_object_or_404(Bookstore, id=bookstore_id)
        serializer = self.serializer_class(bookstore, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bookstore_id):
        bookstore = get_object_or_404(Bookstore, id=bookstore_id)
        bookstore.delete()
        return Response({'success': True})


class ReviewsIndex(APIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, bookstore_id):
        queryset = Review.objects.filter(bookstore=bookstore_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, bookstore_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(bookstore_id=bookstore_id, user=request.user)
            queryset = Review.objects.filter(bookstore=bookstore_id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, IsReviewOwner]

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        self.check_object_permissions(request, review)
        review.delete()
        return Response({"message": "Review deleted successfully."})



class EventsIndex(APIView):
    serializer_class = EventSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, bookstore_id):
        queryset = Event.objects.filter(bookstore_id=bookstore_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, bookstore_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(bookstore_id=bookstore_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    serializer_class = EventSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        serializer = self.serializer_class(event)
        return Response(serializer.data)

    def put(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        serializer = self.serializer_class(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return Response({'message': 'Event deleted successfully.'})


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer