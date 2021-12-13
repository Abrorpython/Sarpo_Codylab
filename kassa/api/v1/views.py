from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import api_view


from kassa.models import Income, Expense
from .serializers import IncomeSerializer, ExpenseSerializer


@api_view(['GET'])
def listIncome(request):
    income = Income.objects.all()
    serializer = IncomeSerializer(income, many=True)
    return Response(serializer.data)


class IncomeView(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def list(self, request, *args, **kwargs):
        a = 0
        products = Income.objects.all()
        for i in products:
            a = a + i.income
        return Response({"success": True,
                         "data": a,
                         "message": f"{status.HTTP_200_OK}"
                         })

    def create(self, request, *args, **kwargs):
        serializers = IncomeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                            "success": True,
                            "data": serializers.data,
                            "message": f"{status.HTTP_200_OK}"
                            })
        else:
            return Response({
            "success": serializers.errors,
            "message": f"{status.HTTP_404_NOT_FOUND}"
            })

    def retrieve(self, request, *args, **kwargs):
        income = Income.objects.get(pk=kwargs['pk'])
        serializer = IncomeSerializer(income)
        return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                        })

    def update(self, request, *args, **kwargs):
        income = Income.objects.get(pk=kwargs['pk'])
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                            })
        else:
            return Response({
            "success": serializer.errors,
            "message": f"{status.HTTP_404_NOT_FOUND}"
        })

    def destroy(self, request, *args, **kwargs):
        income = Income.objects.get(pk=kwargs['pk'])
        income.delete()
        return Response({"success": True,
                        "message": f"{status.HTTP_204_NO_CONTENT}"
                         })


@api_view(['GET'])
def listExpense(request):
    expense = Expense.objects.all()
    serializer = ExpenseSerializer(expense, many=True)
    return Response(serializer.data)


class ExpenseView(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def list(self, request, *args, **kwargs):
        a = 0
        products = Expense.objects.all()
        for i in products:
            a = a + i.expense
        return Response({"success": True,
                         "data": a,
                         "message": f"{status.HTTP_200_OK}"
                         })

    def create(self, request, *args, **kwargs):
        serializers = ExpenseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                            "success": True,
                            "data": serializers.data,
                            "message": f"{status.HTTP_200_OK}"
                            })
        else:
            return Response({
            "success": serializers.errors,
            "message": f"{status.HTTP_404_NOT_FOUND}"
            })

    def retrieve(self, request, *args, **kwargs):
        expence = Expense.objects.get(pk=kwargs['pk'])
        serializer = IncomeSerializer(expence)
        return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                        })

    def update(self, request, *args, **kwargs):
        expence = Expense.objects.get(pk=kwargs['pk'])
        serializer = IncomeSerializer(expence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                            })
        else:
            return Response({
            "success": serializer.errors,
            "message": f"{status.HTTP_404_NOT_FOUND}"
        })

    def destroy(self, request, *args, **kwargs):
        expence = Expense.objects.get(pk=kwargs['pk'])
        expence.delete()
        return Response({"success": True,
                        "message": f"{status.HTTP_204_NO_CONTENT}"
                         })