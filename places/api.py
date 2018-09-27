from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import get_places
from .serializers import PlaceSerializer

@api_view(['GET'])
def get_places(request):
    query = request.GET['query']
    places = get_places(query=query)
    serializer = PlaceSerializer(places, many=True)
    return serializer.data

