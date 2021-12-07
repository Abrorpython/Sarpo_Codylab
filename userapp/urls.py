from django.urls import path, include

urlpatterns = [
    path('v1/', include('userapp.api.v1.urls'))
]