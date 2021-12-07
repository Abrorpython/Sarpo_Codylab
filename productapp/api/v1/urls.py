from django.urls import path

from .views import CategoryView, ProductView, SearchProductCategory, \
    SearchProduct, SearchQRProduct, productListView, CustomView

urlpatterns = [
    path('category/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('category/<int:pk>/', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('product/', ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>/', ProductView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('searchcategory/<int:pk>/', SearchProductCategory.as_view({'get': 'list'})),
    path('', SearchProduct.as_view()),
    path('qr/<int:qr>/', SearchQRProduct.as_view({'get': 'retrieve'})),
    path('karzinka/', productListView),
    path('customer/', CustomView.as_view({'get': 'list', 'post': 'create'})),
    path('customer/<int:pk>/', CustomView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]