from django.urls import path
from . import views 

urlpatterns = [ 
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name='resgister'),
    path('profile/', views.getUserProfile, name = 'get-user-profile'),

    path('categories/', views.getCategoryList, name = 'categories'),
    path('category/<str:id>', views.getCategory, name='category'),
 
    path('products/', views.getProducts, name="products"),
    path('product/<str:id>', views.getProduct_Detail, name="product"),

    path('add-order/', views.addOrderItems, name='order-add'),
    path('get-order/', views.getOrder, name = "get-order-id")
]