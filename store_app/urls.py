from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet)


urlpatterns = [
    path('customers/',views.CustomerList.as_view()),
    path('customers/<int:pk>',views.CustomerDetail.as_view()),
    path('addProductToCustomer/',views.AddProductToCustomer.as_view()),
    path('deleteProductFromCustomer/<int:customer_id>',views.delete_product_from_user)
    
]


urlpatterns += router.urls
