from rest_framework.routers import DefaultRouter
from main.viewset import DeliverViewset, CategoryViewset, ProductViewset, ProductItemViewset

router = DefaultRouter()
router.register("category", CategoryViewset)
router.register("product", ProductViewset)
router.register("productitem", ProductItemViewset)
router.register("deliver", DeliverViewset)
