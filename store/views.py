from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Category, Product
from .serializers import CategoryListSerializer, CategoryDetailSerializer, ProductListSerializer, ProductDetailSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse 


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'categories': reverse('category-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format)
    })


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        query_set = Product.objects.all()

        # filter products by category passed in query string
        category_id = self.request.GET.get('category_id')
        if category_id:
            query_set = query_set.filter(category__id=category_id)
        
        return query_set

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()