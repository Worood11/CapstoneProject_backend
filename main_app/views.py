from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status , generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Bookstore , Review , Event
from .serializers import BookstoreSerializer , ReviewSerializer , UserSerializer , EventSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# User Registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
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
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):

  def post(self, request):
    try:
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        refresh = RefreshToken.for_user(user)
        content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data}
        return Response(content, status=status.HTTP_200_OK)
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the capstone_project api home route!'}
    return Response(content)
  

class BookstoresIndex(APIView):
  serializer_class = BookstoreSerializer

  def get(self, request):
    data = list(Bookstore.objects.values())
    
    try:
      queryset = Bookstore.objects.all()
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def post(self, request, *args, **kwargs):
    try:
      print(request.data, "line 30 views")
      serializer = self.serializer_class(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BookstoreDetail(APIView):
    serializer_class = BookstoreSerializer

    def get(self, request, bookstore_id):
        try:
            bookstore = get_object_or_404(Bookstore, id=bookstore_id)
            serializer = self.serializer_class(bookstore)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, bookstore_id):
        try:
            bookstore = get_object_or_404(Bookstore, id=bookstore_id)
            serializer = self.serializer_class(bookstore, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, bookstore_id):
        try:
            bookstore = get_object_or_404(Bookstore, id=bookstore_id)
            bookstore.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class ReviewsIndex(APIView):
    serializer_class = ReviewSerializer

    def get(self, request, bookstore_id):
        try:
            queryset = Review.objects.filter(bookstore=bookstore_id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, bookstore_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(bookstore_id=bookstore_id)  
            queryset = Review.objects.filter(bookstore=bookstore_id)
            reviews = self.serializer_class(queryset, many=True)
            return Response(reviews.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class ReviewDetail(APIView):
    def delete(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
            review.delete()
            return Response({"message": "Review deleted successfully."}, status=status.HTTP_200_OK)
        except Review.DoesNotExist:
            return Response({"error": "Review not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class EventsIndex(APIView):
    serializer_class = EventSerializer

    def get(self, request, bookstore_id):
      
        try:
            queryset = Event.objects.filter(bookstore_id=bookstore_id)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, bookstore_id):
    
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(bookstore_id=bookstore_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EventDetail(APIView):
    serializer_class = EventSerializer

    def get(self, request, event_id):
    
        try:
            event = get_object_or_404(Event, id=event_id)
            serializer = self.serializer_class(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, event_id):
        
        try:
            event = get_object_or_404(Event, id=event_id)
            serializer = self.serializer_class(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, event_id):
       
        try:
            event = get_object_or_404(Event, id=event_id)
            event.delete()
            return Response({'message': 'Event deleted successfully.'}, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer