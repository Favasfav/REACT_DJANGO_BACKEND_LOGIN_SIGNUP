from rest_framework import serializers

from rest_framework.serializers import ModelSerializer, ValidationError, ImageField
# from base.models import Note
# from django.contrib.auth.models import User
from base.models import Profile



# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'



class RegistrationSerializer(serializers.ModelSerializer):
    
    

    def create(self, validated_data):
        print('nnnnnnnnnnnnnnnnnnnnnnnnnnn')
        username = validated_data['username']
        password = validated_data['password']

        # Check if the username already exists
        if Profile.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'This username is already in use.'})
        
        user = Profile(username=username)
        user.set_password(password)
        user.save()
        return user
    class Meta:
        model = Profile
        fields = ('username', 'password')    


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'bio', 'profile_image']    
class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'bio', 'profile_image']         


class UserUpdateSerializer(serializers.ModelSerializer):
    print('------------UserUpdateSerializer')
    class Meta:
        model = Profile
        fields = ['username','bio', 'profile_image']     
# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['username']           