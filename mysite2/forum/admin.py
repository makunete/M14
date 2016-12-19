from django.contrib import admin

# Register your models here.
from .models import Login

admin.site.register(Login)

from .models import Missatges

admin.site.register(Missatges)

from .models import Hashtags

admin.site.register(Hashtags)