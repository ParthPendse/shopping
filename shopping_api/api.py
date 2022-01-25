from rest_framework import generics

from rest_framework.response import Response

from .serializers import CartSerializer

from .models import Cart




class CartCreateApi(generics.CreateAPIView):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer

class CartListApi(generics.ListAPIView):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer

class CartDestroyApi(generics.DestroyAPIView):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer

class CartUpdateApi(generics.RetrieveUpdateAPIView):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer