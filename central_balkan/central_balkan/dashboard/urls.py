from django.urls import path
from .views import MainPageView, CategoryDetailView, AskQuestionView, AboutUsView

app_name = "dashboard"

urlpatterns = [
    path('', view=MainPageView.as_view(), name="main-page"),
    path('about-us/', view=AboutUsView.as_view(), name="about_us"),
    path(
        'category/<str:category_slug>/',
        view=CategoryDetailView.as_view(),
        name='category_detail'
    ),
    path(
        'ask_question',
        view=AskQuestionView.as_view(),
        name='ask_question'
    ),
]
