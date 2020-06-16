from django.urls import path

from central_balkan.products.apis import CategoriesAndProductsAPIView, ProductsDetailAPIView

app_name = 'products'
urlpatterns = [
    path('', view=CategoriesAndProductsAPIView.as_view()),
    path('<int:product_id>/', view=ProductsDetailAPIView.as_view()),
]
