from rest_framework.serializers import ModelSerializer
from main.models import Category, Product, ProductItem, Deliver


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductReadSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"


class DeliverSerializer(ModelSerializer):
    class Meta:
        model = Deliver
        fields = "__all__"


class ProductItemReadSerializer(ModelSerializer):
    product = ProductReadSerializer(read_only=True)
    deliver = DeliverSerializer(read_only=True)

    class Meta:
        model = ProductItem
        fields = "__all__"


class ProductItemSerializer(ModelSerializer):
    class Meta:
        model = ProductItem
        fields = "__all__"
