from rest_framework import serializers 
from django.contrib.auth.models import User
from .models import Profile

class User_Serializer(serializers.ModelSerializer):

	class Meta:

		model = User 
		fields = ["url" ,"username", "email"]




class Profile_Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:

		model = Profile 
		fields = ["url", "user"]
