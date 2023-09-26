from django.urls import path 
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
   
    TokenRefreshView,
)

urlpatterns=[
    path('',views.getRoutes ),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
   
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    
    path('signup/',views.signup_view),
    path('get_user_profile/<int:user_id>/', views.get_user_profile),
    path('get_userlist', views.get_userlist),
    path('update_user_profile/<int:user_id>/', views.update_user_profile),
     path('get_usertodelete/<int:user_id>/', views.get_usertodelete),
    path('update_user/<int:user_id>/', views.update_user),

   
]