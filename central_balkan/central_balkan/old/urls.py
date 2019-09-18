from django.urls import path

from central_balkan.old.views import OldTemplateView


urlpatterns = [
    path(
        '<str:template_name>/',
        OldTemplateView.as_view()
    )
]
