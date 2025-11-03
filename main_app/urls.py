from django.urls import path
from .views import Home , BookstoresIndex , BookstoreDetail , ReviewsIndex , ReviewDetail , CreateUserView , LoginView , EventsIndex , EventDetail, EventListCreateView 
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('bookstores/', BookstoresIndex.as_view(), name='bookstore-index'),
    path('bookstores/<int:bookstore_id>/', BookstoreDetail.as_view(), name='bookstore-detail'),
    path('bookstores/<int:bookstore_id>/reviews/', ReviewsIndex.as_view(), name='review-create'),
    path('reviews/<int:review_id>/', ReviewDetail.as_view(), name='review-detail'),
    path('bookstores/<int:bookstore_id>/events/', EventsIndex.as_view(), name='events-index'),
    path('events/<int:event_id>/', EventDetail.as_view(), name='event-detail'),
    path('events/', EventListCreateView.as_view(), name='events-list'), 
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),



]