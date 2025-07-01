from rest_framework import viewsets, permissions
from .models import Cat
from .serializers import CatSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['breed', 'gender', 'age', 'owner']
    search_fields = ['name', 'breed']
    ordering_fields = ['created_at', 'age']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

