from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view

from .serializers import CategorySerializers, ProductSerializers, CustomerSerializers
from productapp.models import Category, Product, Customer


class CustomView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    def list(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializers = CustomerSerializers(customers, many=True)
        return Response({"success": True,
                         "data": serializers.data,
                         "message": f"{status.HTTP_200_OK}"
                         })

    def create(self, request, *args, **kwargs):
        serializers = CustomerSerializers(data=request.data)
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
        customer = Customer.objects.get(pk=kwargs['pk'])
        serializer = CustomerSerializers(customer)
        return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                        })

    def update(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=kwargs['pk'])
        serializer = CustomerSerializers(customer, data=request.data)
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
        customer = Customer.objects.get(pk=kwargs['pk'])
        customer.delete()
        return Response({"success": True,
                        "message": f"{status.HTTP_204_NO_CONTENT}"
                         })


# for karzinka
@api_view(['GET'])
def productListView(request):
    if request.method == 'GET':
        product = [1]
        for i in product:
            queryset = Product.objects.get(pk=i)
            serializer = ProductSerializers(queryset, many=True)
            return Response({'ok': serializer.data})


# search Q/R kod bo'yicha
class SearchQRProduct(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def retrieve(self, request, *args, **kwargs):
        product = Product.objects.get(qr=kwargs['qr'])
        serializer = ProductSerializers(product)
        return Response({"success": True,
                         "data": serializer.data,
                         "message": f"{status.HTTP_201_CREATED}"
                         })



# Mahsulotni qidirish nomi bo'yicha
class SearchProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['^name']


# Categoriya bo'yicha qidiruv
class SearchProductCategory(ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(category_id=kwargs['pk'])
        serializers = ProductSerializers(queryset, many=True)
        return Response({"success": True,
                         "data": serializers.data,
                         "message": f"{status.HTTP_200_OK}"
                         })

# for Product
class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializers = ProductSerializers(products, many=True)
        return Response({"success": True,
                         "data": serializers.data,
                         "message": f"{status.HTTP_200_OK}"
                         })

    def create(self, request, *args, **kwargs):
        serializers = ProductSerializers(data=request.data)
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
        product = Product.objects.get(pk=kwargs['pk'])
        serializer = ProductSerializers(product)
        return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                        })

    def update(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['pk'])
        serializer = ProductSerializers(product, data=request.data)
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
        product = Product.objects.get(pk=kwargs['pk'])
        product.delete()
        return Response({"success": True,
                        "message": f"{status.HTTP_204_NO_CONTENT}"
                         })


# For category
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def list(self, request, *args, **kwargs):
        categorys = Category.objects.all()
        serializers = CategorySerializers(categorys, many=True)
        return Response({"success": True,
                         "data": serializers.data,
                         "message": f"{status.HTTP_200_OK}"
                         })

    def create(self, request, *args, **kwargs):
        serializers = CategorySerializers(data=request.data)
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
        category = Category.objects.get(pk=kwargs['pk'])
        serializer = CategorySerializers(category)
        return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                        })

    def update(self, request, *args, **kwargs):
        category = Category.objects.get(pk=kwargs['pk'])
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                            "data": serializer.data,
                            "message": f"{status.HTTP_201_CREATED}"
                            })
        else:
            return Response({
            "success": False,
            "message": f"{status.HTTP_404_NOT_FOUND}"
        })

    def destroy(self, request, *args, **kwargs):
        category = Category.objects.get(pk=kwargs['pk'])
        category.delete()
        return Response({"success": True,
                        "message": f"{status.HTTP_204_NO_CONTENT}"
                         })



