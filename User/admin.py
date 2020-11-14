from django.contrib import admin
from .models import Packages
from .models import Prediction
# Register your models here.
admin.site.register(Packages)
admin.site.register(Prediction)
