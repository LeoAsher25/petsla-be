from django.contrib.auth.models import update_last_login
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from django.contrib.auth.models import User 

from store.models import Product, Order, OrderItem, Category
from store.serializers import ProductSerializer, CategorySerializer, OrderSerializer, UserSerializer, UserSerializerWithToken

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def addOrderItems(request): 
    user = request.user
    data = request.data
    orderItems = data['orderItems'] 

    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'Không có sản phẩm!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create( 
            user = user,
            number_phone = data['number_phone'],
            address = data['address'],
            total_price = data['total_price'], 
        )

        for i in orderItems:
            product = Product.objects.get(id=i['product_id'])

            item = OrderItem.objects.create(
                product = product,
                order = order,
                name = product.product_name,
                quantity = i['quantity'],
                price = i['price'],
                image = "http://127.0.0.1:8000"+product.images.url,
            )

            product.stock -= item.quantity
            product.save()
        serializer = OrderSerializer(order, many = False)
        return Response(serializer.data)

#
@api_view(['GET'])
def getCategory(request, id):
    if id != None:
        categories = get_object_or_404(Category, id = id)
        products = Product.objects.filter(category=categories)
    else:
        products = Product.objects.all()    
    serializers = ProductSerializer(products, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getCategoryList(request):
    category = Category.objects.all()
    serializers = CategorySerializer(category, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def getProduct_Detail(request, id):
    product = Product.objects.get(id=id)
    serializers = ProductSerializer(product, many=False)
    return Response(serializers.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': ('Tài khoản hoặc mật khẩu không chính xác!')
    }
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            username = data['username'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Tên đăng nhập đã được sử dụng!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many = False) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrder(request):
    user = request.user
    orders = user.order_set.all() 
    serializer = OrderSerializer(orders, many = True)
    return Response(serializer.data)