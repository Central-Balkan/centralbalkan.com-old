from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.db.models import Count

from central_balkan.common.utils import inline_serializer
from central_balkan.products.models import Category


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
