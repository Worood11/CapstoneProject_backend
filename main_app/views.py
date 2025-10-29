from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Bookstore
from .serializers import BookstoreSerializer

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
