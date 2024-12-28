from dataclasses import fields
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser,Customer,Contact

# Register your models here.
fields =list(UserAdmin.fieldsets)
fields[1] =('Personal Info',{'fields':('first_name','last_name','email','mobile')})
UserAdmin.fieldsets=tuple(fields)

admin.site.register(NewUser,UserAdmin)
admin.site.register(Customer)
admin.site.register(Contact)