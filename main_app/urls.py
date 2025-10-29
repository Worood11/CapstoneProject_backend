from django.urls import path
from .views import Home , BookstoresIndex , BookstoreDetail , ReviewsIndex
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('bookstores/', BookstoresIndex.as_view(), name='bookstore-index'),
    path('bookstores/<int:bookstore_id>/', BookstoreDetail.as_view(), name='bookstore-detail'),
    path('bookstores/<int:bookstore_id>/reviews/', ReviewsIndex.as_view(), name='review-create'),


]