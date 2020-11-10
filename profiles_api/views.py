from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
      """Test API View"""
      serializer_class = serializers.HelloSerializer

      def get(self, request, format=None):
            """Returns a list of APIView features"""
            an_apiview = [
                  'Uses HTTP methods as function (get, post, patch, put, delete)',
                  'Is similar to a traditional Django View',
                  'Gives you the most control over your application logic',
                  'Is mapped manually to URLs',
            ]

            return Response({'message': 'hello!', 'an_apiview': an_apiview})
      
      def post(self, request):
            """Create a hello message with our name"""
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                  name = serializer.validated_data.get('name')
                  message = f"Hello, {name}"
                  return Response({'message': message})
            
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      # PATCH: to do an update, but only update the fields that were provided in the REQUEST. If you had a first name and a last name field, 
      # and you made a PATCH request with just providing the "last name". It would only update the "last name".

      # PUT: whereas, if you did a PUT request, and you only provided the last name. Then, in that case it would remove the first name completely.
      # Because, HTTP PUT is basically replacing an object with the object that was provided.

      def put(self, request, pk=None):
            """Handle updating an object"""
            return Response({'method': 'PUT'})
      
      def patch(self, request, pk=None):
            """Handle a partial update of an object"""
            return Response({'method': 'PATCH'})

      def delete(self, request, pk=None):
            """Delete an object"""
            return Response({'method': 'DELETE'})
