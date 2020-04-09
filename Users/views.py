from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializers import User_Serializer, Profile_Serializer
from .models import Profile
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
"""
class User_Viewset(viewsets.ViewSet):


	def list(self, request):
	
		queryset = User.objects.all()
		serializer = User_Serializer(queryset, many=True, context={"request":request})

		return Response(data=serializer.data)

	def retrieve(self, request, pk=None):

		queryset = User.objects.get(pk=pk)
		user = get_object_or_404(queryset)
		serializer = User_Serializer(user)

		return Response(serializer.data) 

"""

class UserViewSet(ModelViewSet):

	serializer_class = User_Serializer
	queryset =  User.objects.all()

class ProfileViewSet(ModelViewSet):

	serializer_class = Profile_Serializer
	queryset = Profile.objects.all()

