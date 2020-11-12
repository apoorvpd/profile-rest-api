from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Token Authentication: is the type of authentication we use for users to authenticate themselves with our API.
# It works by generating a random token string when the user logs in, and then every request we make to that API
# we add this token string to the request, and that's effectively a password to check every request made is authenticated correctly.
from rest_framework.authentication import TokenAuthentication


from rest_framework import filters
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

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


class HelloViewSet(viewsets.ViewSet):
      """Test API ViewSet"""
      serializer_class = serializers.HelloSerializer

      def list(self, request):
            """Return a hello message"""

            a_viewset = [
                  'Uses actions (list, create, retrieve, update, partial_update)',
                  'Automatically maps to URLs using Routers',
                  'Provides more functionality with less code',
                  ]

            return Response({'message': 'Hello!', 'a_viewset': a_viewset})
      

      def create(self, request):
            """Create a new hello message"""
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                  name = serializer.validated_data.get('name')
                  message = f'Hello {name}!'
                  return Response({'message': message})
            
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

      def retrieve(self, request, pk=None):
            """Handle getting an object by its ID"""
            return Response({'http_method': 'GET'})
      
      def update(self, request, pk=None):
            """Handle updating an object"""
            return Response({'http_method': 'PUT'})
      
      def partial_update(self, request, pk=None):
            """Handle updating part of an object"""
            return Response({'http_method': 'PATCH'})
      
      def destroy(self, request, pk=None):
            """Handle removing an object"""
            return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
      """Handle creating and updating profiles"""
      serializer_class = serializers.UserProfileSerializer
      queryset = models.UserProfile.objects.all()
      authentication_classes = (TokenAuthentication,)
      # Permission Class: how the user gets permission to do certain things.
      # So, you may have an authenticated userwho has permission to do certain things or use certain APIs,
      # but not the other APIs.
      # You can control those fine grained permissions by using Permission classes.
      permission_classes = (permissions.UpdateOwnProfile,)
      filter_backends = (filters.SearchFilter, )
      search_fields = ('name', 'email', ) # search by name or email field.


class UserLoginApiView(ObtainAuthToken):
      """Handle creating user authentication tokens"""
      renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
      