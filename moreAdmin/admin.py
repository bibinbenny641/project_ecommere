from webbrowser import get
from django.contrib import admin
from django.contrib.auth import get_user_model

from moreAdmin.models import User


# Register your models here.
User = get_user_model()


admin.site.register(User)