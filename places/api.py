from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import get_places as get_places_details
from .serializers import PlaceSerializer

@api_view(['GET'])
def get_places(request):
    query = request.GET['query']
    places = get_places_details(query=query)
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

