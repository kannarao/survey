from django.contrib import admin

from .models import Service,Answers

class AnswersAdmin(admin.ModelAdmin):
	list_display = ("ans1","ans2","ans3")

admin.site.register(Service)
admin.site.register(Answers,AnswersAdmin)
