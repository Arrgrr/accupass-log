from django.contrib import admin
from log.models import Log, Category, User


admin.site.register(Log)
admin.site.register(User)
admin.site.register(Category)
