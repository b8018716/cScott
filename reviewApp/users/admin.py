from pyexpat import model
from django.contrib import admin
from . models import Profile
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.admin import UserAdmin

class ProfileInLine(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_superuser', 'is_staff'),
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username','email','is_staff','last_login','date_joined')
    
    inlines = [ProfileInLine]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name')



admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
