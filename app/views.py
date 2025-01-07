from django.shortcuts import render
from .models import ProductType,Product,Purchase,Vendor,Sell,Department
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .seriallizers import ProductTypeSerializer, ProductSerializer, PurchaseSerializer, DepartmentSerializer, VendorSerializer, SellSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
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


