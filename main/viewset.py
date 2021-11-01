from django.db.models import Sum, F
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from main.serializer import DeliverSerializer, CategorySerializer, ProductSerializer, ProductItemSerializer, \
    ProductItemReadSerializer
from main.models import Category, Product, ProductItem, Deliver


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post']

    @action(methods=['GET'], detail=False)
    def get_product_data(self, request):
        pk = int(request.GET.get("pk", 0))
        if pk > 0:
            try:
                items = list(ProductItem.objects.filter(product__category__in=[pk]) \
                    .values('product', "product__name").annotate(
                    jami_soni=Sum(F("quantity")), jami_summa=Sum(F("quantity") * F("price"))
                ))
                return Response(items)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        else:
            return Response({"error": "pk is not defined"}, status=400)


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post']


class ProductItemViewset(ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    http_method_names = ['get', 'post']

    @action(methods=['GET'], detail=False)
    def get_product_item(self, request):
        pk = int(request.GET.get("pk", 0))
        if pk > 0:
            try:
                items = ProductItem.objects.filter(product_id=pk, quantity__gt=0)
                return Response(ProductItemReadSerializer(items, many=True).data)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        else:
            return Response({"error": "pk is not defined"}, status=400)

    @action(methods=['GET'], detail=False)
    def get_benefit_order(self, request):
        items = list(ProductItem.objects.filter(quantity__gt=0)
                     .values('product', "product__name").annotate(
            foyda=Sum(F("quantity") * (F("price") - F("base_price")))
        ).order_by("-foyda"))
        return Response(items)


class DeliverViewset(ModelViewSet):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
    http_method_names = ['post']
