from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Class)
admin.site.register(News)
admin.site.register(Quize)
admin.site.register(Question)
admin.site.register(Answer)