from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import os
from rest_framework import permissions
from .views import authentification_view
from rest_framework_simplejwt.views import TokenBlacklistView

schema_view = get_schema_view(
    openapi.Info(
        title="Django Template Swagger",
        default_version='v1',
        description="API Documentation for Django Template",
        contact=openapi.Contact(url="https://github.com/BastianLo/django-template"),
        license=openapi.License(name="Apache-2.0 license "),
    ),
    public=False,
    #permission_classes=[permissions.IsAuthenticated, ],
)

urlpatterns = [
    path('', RedirectView.as_view(url='swagger/')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
    path('auth/token/', authentification_view.ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('auth/me/', authentification_view.current_user, name='current_user'),
    path('auth/refresh/', authentification_view.RefreshTokenView.as_view(), name='token_obtain_pair'),
]