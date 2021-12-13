from django.urls import path

from .views import IncomeView, ExpenseView
from .views import listIncome, listExpense

urlpatterns = [
    path('income/', IncomeView.as_view({'get': 'list', 'post': 'create'})),
    path('income-list/<int:pk>/', IncomeView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('income-list/', listIncome),
    path('expence/', ExpenseView.as_view({'get': 'list', 'post': 'create'})),
    path('expence-list/<int:pk>/', ExpenseView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('expence-list/', listExpense)
]