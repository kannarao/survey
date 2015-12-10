from django.forms import ModelForm
from app.models import *

class FirstForm(ModelForm):
	class Meta:
		model = Answers
		fields = ('ans1','ans2','ans3')

