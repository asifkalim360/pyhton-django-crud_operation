from django.contrib import admin
from .models import User            #model se user ko import karna hoga
# Register your models here.
@admin.register(User)               #register karna hoga apne User ko.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')