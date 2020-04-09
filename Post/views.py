from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import Post_Serializer, Comment_Serializer
from .models import Post, Comment
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle
from Users.models import Profile
# Create your views here.


class Post_ViewSet(ModelViewSet):

	serializer_class = Post_Serializer
	queryset = Post.objects.all()
	lookup_field = "slug"
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	throttle_scope = "post"
	throttle_classes = (ScopedRateThrottle, )
	filter_fields = ("titre", "auteur")
	search_fields = ("^titre", )
	ordering_fields = ("titre", "date")

	def perform_create(self, serializer):
		profile_obj = get_object_or_404(Profile, user=self.request.user)

		serializer.save(auteur=profile_obj)


class Comment_View(ModelViewSet):

	queryset = Comment.objects.all()
	serializer_class = Comment_Serializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		profile_obj = get_object_or_404(Profile, user=self.request.user)

		serializer.save(auteur=profile_obj)



"""
class Comment_View(mixins.CreateModelMixin,
					mixins.ListModelMixin,
					mixins.RetrieveModelMixin,
					GenericViewSet):

	queryset = Comment.objects.all()
	serializer_class = Comment_Serializer

	def list(self, request, *args, **kwargs):

		queryset = self.get_queryset()
		serializer = Comment_Serializer(queryset, many=True, context={"request":request})

		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		
		serializer = self.get_serializer(data=request.data, many=True)

		if serializer.is_valid():
			serializer.save()
		
		return Response(serializer.data)

	def update(self, request, *args, **kwargs):

		obj = self.get_object()
		serializer = self.get_serializer(obj,data=request.data)
		serializer.is_valid(raise_exception=True)

		return Response(serializer.data)

	def destroy(self, request, *args, **kwargs):

		obj = self.get_object()
		self.perform_destroy(obj)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance):

		instance.delete()



class Comment_View(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Comment.objects.all()

	def retrieve(self, request, *args, **kwargs):
		#print(self.kwargs)
		#pk = self.kwargs.get('pk')
		comment_objs = Comment.objects.all()
		serializer = Comment_Serializer(comment_objs)

		return Response(serializer.data)


class Comment_View(generics.ListCreateAPIView):

	serializer_class = Comment_Serializer
	queryset = Comment.objects.all()

	def list(self, request):

		queryset = self.get_queryset()
		serializer = Comment_Serializer(queryset, many=True)

		return Response(serializer.data)



class Comment_View(generics.GenericAPIView):

	name = 'api-root'

	def get(self, request, *args, **kwargs):
		
		return Response({
		'post': reverse(Post.name, request=request),
		'game-categories': reverse(GameCategoryList.name, request=request),
		'games': reverse(GameList.name, request=request),
		'scores': reverse(PlayerScoreList.name, request=request)
		})

"""