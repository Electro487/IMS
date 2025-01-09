from django.shortcuts import render
from .models import ProductType,Product,Purchase,Vendor,Sell,Department
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .seriallizers import ProductTypeSerializer, ProductSerializer, PurchaseSerializer, DepartmentSerializer, VendorSerializer, SellSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class ProductTypeView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductView(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self,request):
        product_objs = self.get_queryset()
        serializer = self.get_serializer(product_objs,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:                                            #if request is sent from user you must send response
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)       

    def retrieve(self, request, pk):
        # try:
        #     product_obj = Product.objects.get(id=pk) self.get_object() 
        #     serializer = self.get_serializer(product_obj)
        #     return Response(serializer.data)
        # except:
        #     return Response("Data not found!", status=status.HTTP_404_NOT_FOUND)
        # ORRRRR: self.get_object() does this in default
        product_obj = self.get_object()
        serializer = self.get_serializer(product_obj)
        return Response(serializer.data)

    def update(self, request, pk):
        product_obj = self.get_object()
        serializer = self.get_serializer(instance=product_obj, data=request.data) # instance=old one and data is new one
        if serializer.is_valid(): # Upto above it just creates a object but it is not updated yet.Saving will update it so:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST) # here posiitionally status is second so no need to write status=

    def destroy(self, request, pk):
        product_obj = self.get_object()
        product_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["POST"])
def register_view(request):
    password = request.data.get("password")
    hash_password = make_password(password)
    data = request.data.copy()
    data["password"] = hash_password
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user == None:
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)

class PurchaseView(GenericViewSet):
    queryset = Purchase.objects.all()
    serizlizer_class = PurchaseSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)


class VendorView(GenericViewSet):
    
    queryset = Vendor.objects.all()
    serizlizer_class = VendorSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


class SellView(GenericViewSet):
    queryset = Sell.objects.all()
    serizlizer_class = SellSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


class DepartmentView(GenericViewSet):
    queryset = Department.objects.all()
    serizlizer_class = DepartmentSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


