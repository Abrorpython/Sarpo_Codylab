from django.urls import path

from .views import RegistrationView, \
                    LoginAPIView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]