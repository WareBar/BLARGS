from django import forms
from . import models


# form for creating a post, used to save time instead of hardcoding from the scratch
class createPost(forms.ModelForm):
	class Meta:
		model = models.Post
		fields = ['title','content','banner',]