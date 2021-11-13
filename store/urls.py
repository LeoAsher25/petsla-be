from django.urls import path
from . import views 

urlpatterns = [ 
    path('user/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/register', views.registerUser, name='resgister'),

    path('categories/', views.getCategoryList, name = 'categories'),
    path('category/<str:id>', views.getCategory, name='category'),
 
    path('products/', views.getProducts, name="products"),
    path('product/<str:id>', views.getProduct_Detail, name="product"),

    path('user/profile', views.getUserProfile, name = 'get-user-profile'),

    path('order/add/', views.addOrderItems, name='order-add'),
    path('get/order/', views.getOrder, name = "get-order-id")
]