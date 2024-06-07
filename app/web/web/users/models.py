# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from .validations import validate_phone_number, validate_email, validate_name, validate_last_name, validate_brithday


class User(AbstractUser):
    name = models.CharField(max_length=50, validators=[validate_name], verbose_name=_('Name'))
    last_name = models.CharField(max_length=50, validators=[validate_last_name], verbose_name=_('Last Name'))
    phone_number = models.CharField(max_length=11, unique=True, validators=[validate_phone_number],
                                    verbose_name=_('Phone Number'))
    email = models.EmailField(unique=True, validators=[validate_email], verbose_name=_('Email'))
    role = models.CharField(max_length=20, choices=[
        ('client', _('Client')),
        ('rescuer', _('Rescuer')),
        ('admin', _('Admin')),
        ('super_admin', _('Super Admin'))
    ], verbose_name=_('Role'))
    address = models.TextField(blank=True, null=True, verbose_name=_('Address'))
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True,
                                      verbose_name=_('Profile Photo'))
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name=_('Balance'))
    date_of_birth = models.DateField(blank=True, null=True, validators=[validate_brithday],
                                     verbose_name=_('Date of Birth'))
    gender = models.CharField(max_length=10, choices=[
        ('male', _('Male')),
        ('female', _('Female'))
    ], blank=True, null=True, verbose_name=_('Gender'))
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_('Avatar'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Is Staff'))
    last_login = models.DateTimeField(blank=True, null=True, verbose_name=_('Last Login'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Joined'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups'),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    def __str__(self):
        return self.username
