from django.urls import path, include 
from .views import Post_ViewSet, Comment_View
from rest_framework.routers import DefaultRouter, url
from .models import Comment
from .serializers import Comment_Serializer
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()


router.register("posts", Post_ViewSet)
router.register("comments", Comment_View)
post_list = Post_ViewSet.as_view({"get":"list", "post":"create"})
post_detail = Post_ViewSet.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})
comment_list = Comment_View.as_view({"get": 'list', "post":"create"})
comment_detail = Comment_View.as_view(
				{"get":"retrieve", "put":"update", "delete":"destroy"}

								)
comment_update = Comment_View.as_view({"get":"retrieve", "put":"update"})
comment_delete = Comment_View.as_view({"get":"retrieve", "delete":"destroy"})

urlpatterns = [
		path("posts/", post_list, name="post-list"),
		path("posts/<slug:slug>/", post_detail, name="post-detail"),
		path("comments/", comment_list, name="comment-list"),
		path("comments/<int:pk>/", comment_detail, name="comment-detail"),
		path("comments/<int:pk>/", comment_update, name="comment-update"),
		path("comments/<int:pk>/", comment_delete, name="comment-delete"),
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json"])

#urlpatterns = router.urls
