from django.urls import path, include

urlpatterns = [
    path('v1/', include('kassa.api.v1.urls'))
]