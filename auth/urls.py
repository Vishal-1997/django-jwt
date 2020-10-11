from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from auth.views import HelloView, Login

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('refresh-token/', TokenRefreshView.as_view()),
]
