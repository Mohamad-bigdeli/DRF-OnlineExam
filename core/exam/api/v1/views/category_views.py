from rest_framework import viewsets, mixins
from ..serializers import (CategorySerializer, 
        FavoriteCategoryCreateSerializer, FavoriteCategoryListRetrieveSerializer)
from ....models import Category, FavoriteCategory
from rest_framework.permissions import (SAFE_METHODS, AllowAny, IsAuthenticated, IsAdminUser)
from authentication.permissions import IsStudent

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser(), IsAuthenticated()]

class FavoriteCategoryViewSet(
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated, IsStudent]

    def get_serializer_class(self):
        if self.action == "create":
            return FavoriteCategoryCreateSerializer
        return FavoriteCategoryListRetrieveSerializer
    
    def get_queryset(self):
        return (FavoriteCategory.objects.select_related("category")
                .filter(student_id=self.request.user.id).all()
        )
    
    def get_serializer_context(self):
        return {"user_id":self.request.user.id}
