from rest_framework import serializers
from productapp.models import Category, Product, Customer


class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'name', 'number', 'descriptions']

    def validate_name(self, value):
        name_query = Customer.objects.filter(name=value)
        if name_query.exists():
            raise serializers.ValidationError("Ushbu mijoz ro'yxatda mavjud")
        return value


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'date']

    def validate_name(self, value):
        name_query = Category.objects.filter(name=value)
        if name_query.exists():
            raise serializers.ValidationError("Ushbu bo'lim oldin mavjud")
        return value


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        model = Product
        fields = ['id', 'category', 'name', 'amount', 'parametr', 'image', 'qr', 'sel_price',
                  'finish_price', 'date', 'descriptions', 'status']

    def validate_name(self, value):
        name_query = Product.objects.filter(name=value)
        if name_query.exists():
            raise serializers.ValidationError('Ushbu mahsulot oldin mavjud')
        return value