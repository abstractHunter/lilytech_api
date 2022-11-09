from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

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
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query_set = Product.objects.all()

        # filter products by category passed in query string
        category_id = self.request.GET.get('category_id')
        if category_id:
            query_set = query_set.filter(category__id=category_id)
        
        return query_set