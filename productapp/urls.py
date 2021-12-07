from django.urls import path, include

urlpatterns = [
    path('v1/', include('productapp.api.v1.urls'))
]