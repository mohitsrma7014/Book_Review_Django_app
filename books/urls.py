from django.urls import path, include
from .views import BookViewSet, ReviewViewSet, register_user
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)
# Nested route for reviews
book_reviews = ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
urlpatterns = [
    
    path('', include(router.urls)),
    path('register/', register_user, name='register_user'),
    path('books/<int:book_pk>/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:book_pk>/reviews/', ReviewViewSet.as_view({'post': 'create'})),  # POST for creating reviews
]
