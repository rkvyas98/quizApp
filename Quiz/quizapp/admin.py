from django.contrib import admin

# Register your models here.
from .models import Question, Test_stat

admin.site.register(Question)
admin.site.register(Test_stat)