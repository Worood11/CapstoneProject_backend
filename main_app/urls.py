from django.urls import path
from .views import Home , BookstoresIndex , BookstoreDetail
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('bookstores/', BookstoresIndex.as_view(), name='bookstore-index'),
    path('bookstores/<int:bookstore_id>/', BookstoreDetail.as_view(), name='bookstore-detail'),


]