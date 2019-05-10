from rest_framework import generics
from rest_framework import permissions

from quotes.models import Quotes
from quotes.api.serializers import QuotesSerializer
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.pagination import SmallSetPagination


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quotes.objects.all().order_by('id')
    serializer_class = QuotesSerializer
    permission_classes = [
        IsAdminUserOrReadOnly
    ]
    pagination_class = SmallSetPagination


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [
        IsAdminUserOrReadOnly
    ]
