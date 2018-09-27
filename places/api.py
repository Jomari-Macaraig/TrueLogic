from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_places(request):
    return Response({'message': 'this is a response'})

