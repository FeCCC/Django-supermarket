from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
# Register your models here.


class StaffAdmin(UserAdmin):

    # form = UserChangeForm
    # add_form = UserCreationForm

    list_display = ('st_id', 'username', 'gender', 'depart', 'job', 'phone')
    list_filter = ('depart', 'gender', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'gender', 'depart', 'job', 'phone')}),
        ('Permissions', {'fields': ('is_superuser','is_staff')}),
        ('Groups', {'fields': ('groups',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'groups')
        }),
        (None, {'fields': ('gender', 'depart', 'job', 'phone')})
    )
    search_fields = ('username',)
    ordering = ('st_id',)
    filter_horizontal = ()


admin.site.register(models.Staff, StaffAdmin)
