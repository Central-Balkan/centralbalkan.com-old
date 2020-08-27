from django.urls import path
from .views import MainPageView, CategoryDetailView

app_name = "dashboard"

urlpatterns = [
    path('', view=MainPageView.as_view(), name="main-page"),
    path(
        'category/<str:category_slug>/',
        view=CategoryDetailView.as_view(),
        name='category_detail'
    ),
]
