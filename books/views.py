from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # You may not need to override this if you're not changing its behavior
    # def get_queryset(self):
    #     return super().get_queryset()


from rest_framework.permissions import IsAuthenticated  # Assuming you want to restrict access


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs.get('book_pk')
        if book_id is not None:
            return self.queryset.filter(book_id=book_id)
        return self.queryset.none()  # Return an empty queryset if book_pk is not provided

    def perform_create(self, serializer):
        book_id = self.kwargs.get('book_pk')  # Get the book ID from the URL
        book = Book.objects.get(pk=book_id)  # Get the book instance
        serializer.save(book=book)  # Save the review with the book instance

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])  # This allows unauthenticated access
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_201_CREATED)

# views.py
from django.views.generic import TemplateView
# views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'  # Adjust this line to just 'index.html'
