from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello, World!"})


# Small data load
@api_view(['GET'])
def small(request):
    return Response({"message": "This is a small payload", "data": [1, 2, 3]})

# Medium data load
@api_view(['GET'])
def medium(request):
    medium_data = [{"id": _, "name": "John Doe"} for _ in range(100)]
    return Response({"message": "This is a medium payload", "data": medium_data})

# Heavy data load
@api_view(['GET'])
def heavy(request):
    heavy_data = [{"id": _, "name": "John Doe","username":f"john{_}"} for _ in range(100000)]
    return Response({"message": "This is a heavy payload", "data": heavy_data})