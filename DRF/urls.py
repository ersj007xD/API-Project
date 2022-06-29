from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns=[
  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  path('user_details/', views.userdetails),
  path('userid_details/<int:pk>/', views.userid_details),
  path('profession/', views.professiondetails),
  path('professionid_details/<int:pk>/', views.professionid_details),
  path('add_user/', views.add_user),
  path('add_profession/', views.add_profession),
  path('edit_user/<int:pk>/', views.edit_user),
  path('edit_profession/<int:pk>/', views.edit_profession),
  path('delete_user/<int:pk>/', views.delete_user),
  path('delete_profession/<int:pk/', views.delete_profession),
]