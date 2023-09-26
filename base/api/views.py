from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view 

from base.api.serializers import RegistrationSerializer,UserProfileSerializer,UserUpdateSerializer,UserlistSerializer
from rest_framework import status
from base.models import Profile
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
      
        # ...

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer  
@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     # user=request.user
#     # notes = user.note_set.all()
#     # serializer = NoteSerializer(notes, many = True)
#     return Response(serializer.data)

@api_view(['POST'])
def signup_view(request):
    if request.method == 'POST':
        print('dddddddddddddddd',request.data)

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User successfully registered.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_profile(request,user_id):
    print("get_user_profile")
    try:
        user_profile = Profile.objects.get(id=user_id)
        serializer = UserProfileSerializer(user_profile)
        print(serializer.data,"000000000000000000000000000000")
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response(
            {'detail': 'User profile not found.'},
            status=status.HTTP_404_NOT_FOUND
        )
@api_view(['PUT'])
def update_user_profile(request, user_id):
    # print("update_user_profile",request.data)
    try:
        user_profile = Profile.objects.get(id=user_id)
        print("User Profile Object:", user_profile)
    except Profile.DoesNotExist:
        return Response({'detail': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        print('----------------')
        print("Request Data:", request.data)
        print('----------------')
        serializer = UserUpdateSerializer(user_profile, data=request.data, partial=True)
        print("Serializer Data:", serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            print("Serializer Data------------:", serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        print("Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_userlist(request):
    print('userlists--------------------------------------------')
    try:
        user_profiles = Profile.objects.all()
        print("User Profile Object:", user_profiles)
        serializer = UserlistSerializer(user_profiles, many = True)
        print(serializer.data,"000000000000000000000000000000")
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({'detail': 'User profiles not found'}, status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def get_usertodelete(request,user_id):
    print("get_usertodelete")
    try:
       userprofile=Profile.objects.get(id=user_id)
    
       userprofile.delete()
       
       return Response({"message": "User deleted successfully"}, status=204)
    except User.DoesNotExist:   
    
            return Response({"message": "User not found"}, status=404)


@api_view(['PUT'])
def update_user(request,user_id):
        try:
          user_profile = Profile.objects.get(id=user_id)
          print('oooooooooooooo',user_profile)
        

          if request.method == 'PUT':
        # Pass request.data to the serializer to deserialize and validate the data
            print('oooooooooooooo',user_profile)
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({'message': 'User successfully registered.'}, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
          return Response({'detail': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)       

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

        
    