from django.contrib import admin
from django.urls import path, include
from DRF import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Swagger API SJ",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.pyswagger.shubham.com/",
      contact=openapi.Contact(email="contact@shubham_jain.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DRF.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
