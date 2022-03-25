from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('adress',views.AdressViewSet, basename='adress')
router.register('customer',views.CustomerViewSet)
router.register('products',views.ProductViewSet)

urlpatterns = router.urls
