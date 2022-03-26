from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('adress',views.AdressViewSet, basename='adress')
router.register('products',views.ProductViewSet)


urlpatterns = [
    path('customers/',views.CusomerList.as_view()),
    path('customers/<int:pk>',views.CustomerDetail.as_view()),
    path('addProductToCustomer/',views.AddProductToCusomer.as_view()),
    path('hello/<int:customer_id>',views.delete_product_from_user)
    
]


urlpatterns += router.urls
