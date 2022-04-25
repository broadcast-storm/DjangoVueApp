"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include, re_path
import os
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import index, indexForTest
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from baton.autodiscover import admin

schema_view = get_schema_view(
    openapi.Info(
        title="Яндекс Геймификация API",
        default_version='v1',
        description="Описание моделей и запросов к БД",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', index, name='index'),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),

    # re_path(r'^favicon\.ico$', favicon_view),
    path('main-quest/', index, name='index'),
    path('competitions/', index, name='index'),
    path('competitions/versus/', index, name='index'),
    path('statistics/', index, name='index'),
    path('rating/', index, name='index'),
    path('shop/', index, name='index'),
    path('shop/cart/', index, name='index'),
    path('tests/', index, name='index'),
    path('tests/<int:id>', indexForTest, name='index'),
    path('auth/login/', index, name='index'),
    path('auth/forgot-password/', index, name='index'),
    url(r'^baton/', include('baton.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^auth/', include('djoser.urls')),
    # url(r'^auth/', include('djoser.urls.authtoken')),
    # url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^api/', include('api.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
