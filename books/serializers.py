from rest_framework import serializers
from .models import Book, Review
from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'review_text', 'review_date']

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Include reviews

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'genre', 'reviews']
