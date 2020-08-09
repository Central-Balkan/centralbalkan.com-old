from django.urls import path
from .views import MainPageView

app_name = "dashboard"

urlpatterns = [
    path('', view=MainPageView.as_view(), name="main-page"),
]
