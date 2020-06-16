from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.db.models import Count

from central_balkan.common.utils import inline_serializer
from central_balkan.products.models import Category, Product


class CategoriesAndProductsAPIView(APIView):
    class OutputSerializer(serializers.Serializer):
        categories = inline_serializer(
            fields={
                'id': serializers.IntegerField(),
                'name': serializers.CharField(),
                'products_count': serializers.IntegerField()
            },
            many=True,
            default=[]
        )
        products = serializers.JSONField(default={})

    def get(self, request):
        categories = Category.objects.prefetch_related('products')
        categories_data = categories.values(
            'id',
            'name',
            products_count=Count('products')
        )
        products_data = {
            category.id: [
                {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'image': product.image_url
                } for product in category.products.all()
            ]
            for category in categories
        }

        data = {
            'categories': categories_data,
            'products': products_data
        }

        response = Response(
            data=self.OutputSerializer(data).data,
            headers={
                'Access-Control-Allow-Origin': '*'
            }
        )

        return response


class ProductsDetailAPIView(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        image_url = serializers.CharField()
        description = serializers.CharField()

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)

        return Response(
            data=self.OutputSerializer(product).data,
            headers={
                'Access-Control-Allow-Origin': '*'
            }
        )
