from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from central_balkan.dashboard.views import MainPageView

urlpatterns = [
    path(
        '',
        include("central_balkan.dashboard.urls", namespace="dashboard"),
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + [
    path(
        '<str:something>',
        view=MainPageView.as_view(),
        name=''
    ),
]

handler404 = 'central_balkan.dashboard.views.MainPageView'


if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
