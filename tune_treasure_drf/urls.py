from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path


schema_view = get_schema_view(
   openapi.Info(
      title='TuneTreasure API',
      default_version='v1',
      description='Документация для приложения cats проекта TuneTreasureDRF',
      contact=openapi.Contact(email='admin@tune.com'),
      license=openapi.License(name='BSD License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('api/', include('api.v1.urls', namespace='api_v1')),
   path('admin/', admin.site.urls),
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
       name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
]
