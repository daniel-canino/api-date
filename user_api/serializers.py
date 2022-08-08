from rest_framework  import serializers
from user_api import models

class CreateUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }

class GetUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.HistorialDate
        fields = ('user','init_date', 'end_date')

    

class DateSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.HistorialDate
        fields = ('user','init_date', 'end_date')




    


