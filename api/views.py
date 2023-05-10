from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from orders.models import Order

@api_view(['GET'])
def getData(request):
    items = Order.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)
