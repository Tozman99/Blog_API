from django.db import models
from Users.models import Profile
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):

	auteur = models.ForeignKey(Profile, on_delete=models.CASCADE)
	titre = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)
	slug = models.SlugField(unique=True)
	content = models.CharField(max_length=1000, default="")

	def save(self, *args, **kwargs):

		self.slug = slugify(self.titre)
		super().save()

	def __str__(self):
		
		return self.titre

class Comment(models.Model):

	auteur = models.ForeignKey(Profile, on_delete=models.CASCADE)
	comment = models.CharField(max_length=200)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)