from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('adress',views.AdressViewSet, basename='adress')
router.register('products',views.ProductViewSet)


urlpatterns = [
    path('customers/',views.CusomerList.as_view()),
    path('customers/<int:pk>',views.CustomerDetail.as_view())
]


urlpatterns += router.urls
