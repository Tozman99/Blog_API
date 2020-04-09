from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedIdentityField
from .models import Post, Comment
from rest_framework import serializers 
from rest_framework.request import Request


class Post_Serializer(HyperlinkedModelSerializer):
	
	auteur = serializers.ReadOnlyField(source='auteur.user.username')
	
	class Meta:

		model = Post
		
		fields = ["titre", "auteur", "content", "url"]
		lookup_field = "slug"
		extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class Comment_Serializer(HyperlinkedModelSerializer):
	
	auteur = serializers.ReadOnlyField(source='auteur.user.username')
	view_name = "comment-detail"
	queryset = Comment.objects.all()

	class Meta:

		model = Comment
		fields = ["comment", "auteur", "post", "url"]

		extra_kwargs = {

				"post": {"lookup_field": "slug"},
				#"url": {"view_name": "comment-detail"}

		}
"""
	def get_url(self, obj, view_name, request, format):

		url_kwargs = {

				"post_slug": obj.post.slug,
				"comment_pk": obj.pk

		}

		return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

	def get_object(self, view_name, view_args, view_kwargs):

		lookup_kwargs = {
			"post__slug": view_kwargs["post_slug"],
			"pk": view_kwargs["comment_pk"]

		}

		return self.get_queryset().get(**lookup_kwargs)
"""