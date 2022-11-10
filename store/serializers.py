from rest_framework import serializers
from .models import Category, Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'image')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'banner')


class ProductDetailSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'price', 'stock', 'image', 'slug')


class CategoryDetailSerializer(serializers.ModelSerializer):

    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'banner', 'slug', 'products')


