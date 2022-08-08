from rest_framework.views import exception_handler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  filters, status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user_api import models, serializers, permissions

class CreateUserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.CreateUserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.UserProfile.objects.all()

  


class GetUserVieSet(viewsets.ModelViewSet):
    serializer_class = serializers.GetUserSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.HistorialDate.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
       

        if serializer.is_valid():
            init_date = serializer.validated_data.get('init_date')
            end_date = serializer.validated_data.get('end_date')

            if init_date > end_date:

                message = 'La fecha de inicio no puede ser mayor que la de fin'
                return Response({'message' : message})

            else: 
                result = end_date - init_date
                message = f'Los dias restantes serían {result.days}'
                return Response({'message' : message})


    

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

    


class CalculateDateApiView(APIView):

    serializer_class = serializers.DateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.CalculateDatePermissions,IsAuthenticated)
 
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
       

        if serializer.is_valid():
            init_date = serializer.validated_data.get('init_date')
            end_date = serializer.validated_data.get('end_date')

            if init_date > end_date:

                message = 'La fecha de inicio no puede ser mayor que la de fin'
                return Response({'message' : message})

            else: 
                serializer.save()
                result = end_date - init_date
                message = f'Los dias restantes serían {result.days}'
                return Response({'message' : message})
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



