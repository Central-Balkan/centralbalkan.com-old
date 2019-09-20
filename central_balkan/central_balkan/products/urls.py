from django.urls import path

from central_balkan.products.apis import CategoriesAndProductsAPIView

app_name = 'products'
urlpatterns = [
    path('', view=CategoriesAndProductsAPIView.as_view()),
]
