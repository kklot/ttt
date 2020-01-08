from django.contrib import admin

# Register your models here.
from .models import Question, DuocThu, Tuongtac
admin.site.register(Question)
admin.site.register(DuocThu)
admin.site.register(Tuongtac)