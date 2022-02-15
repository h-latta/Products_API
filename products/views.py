from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def product_list(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)
