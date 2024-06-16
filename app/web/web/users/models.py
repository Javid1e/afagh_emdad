from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from .validations import (validate_name, validate_last_name, validate_birthday, validate_username,
                          validate_phone_number, validate_email, validate_password, validate_url)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True, validators=[validate_username], verbose_name=_('Username'),
                                help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'))
    # //Todo : compelete password help_text
    password = models.CharField(max_length=128, validators=[validate_password], verbose_name=_('Password'),
                                help_text=_('Required. '))
    personal_information = models.OneToOneField('users.PersonalInformation', on_delete=models.CASCADE,
                                                related_name='user', null=True, blank=True)
    account_information = models.OneToOneField('users.AccountInformation', on_delete=models.CASCADE,
                                               related_name='user', null=True, blank=True)
    rsa_information = models.OneToOneField('users.RSAInformation', on_delete=models.CASCADE, related_name='user',
                                           null=True, blank=True)
    # //Todo : compelete groups
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups'),
    )
    # //Todo : compelete user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    class Meta:
        # //Todo : compelete all permissions
        permissions = (
            ("can_view_profile", "Can view profile"),
            ("can_edit_profile", "Can edit profile"),
        )

    def get_username(self):
        return self.username

    def get_password(self):
        return self.account_information.password

    def get_personal_information(self):
        return (f"{self.personal_information.name} {self.personal_information.last_name}"
                f"{self.personal_information.gender}")

    def get_full_name(self):
        return f"{self.personal_information.name} {self.personal_information.last_name}"

    def get_short_name(self):
        return self.personal_information.name

    def get_last_name(self):
        return self.personal_information.last_name

    def get_gender(self):
        return self.personal_information.gender

    def get_birthday(self):
        return self.personal_information.date_of_birth

    def get_address(self):
        return self.personal_information.address

    def get_email(self):
        return self.account_information.email

    def get_phone(self):
        return self.personal_information.phone

    def get_avatar(self):
        return self.personal_information.avatar

    def get_account_role(self):
        return self.account_information.role

    def get_balance(self):
        return self.account_information.balance

    def get_rsa_role(self):
        return self.rsa_information.role

    def get_rating(self):
        return self.rsa_information.rating

    def get_last_login(self):
        return self.account_information.last_login

    def get_date_joined(self):
        return self.account_information.date_joined

    def get_created_at(self):
        return self.account_information.created_at

    def get_updated_at(self):
        return self.account_information.updated_at

    def __str__(self):
        return (f"{get_username(self)} {get_personal_information(self)}"
                f"{get_a} {self.personal_information.last_name}")


class PersonalInformation(models.Model):
    personal_information_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='personal_information')
    name = models.CharField(max_length=50, validators=[validate_name], verbose_name=_('Name'))
    last_name = models.CharField(max_length=50, validators=[validate_last_name], verbose_name=_('Last Name'))
    date_of_birth = models.DateField(blank=True, null=True, validators=[validate_birthday],
                                     verbose_name=_('Date of Birth'))
    gender = models.CharField(max_length=10, choices=[
        ('male', _('Male')),
        ('female', _('Female'))
    ], blank=True, null=True, verbose_name=_('Gender'))
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('Phone'))

    def __str__(self):
        return f"{self.name} {self.last_name}"


class PAAddress(models.Model):
    pa_address_id = models.AutoField(primary_key=True)
    personal_information = models.ForeignKey('users.PersonalInformation', on_delete=models.CASCADE,
                                             related_name='pa_addresses')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Address'))
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('City'))
    state = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('State'))
    zip_code = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Zip Code'))

    def __str__(self):
        return f"{self.address} {self.city} {self.state} {self.zip_code}"


class AccountInformation(models.Model):
    account_information_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='account_information')
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name=_('Phone Number'),
                                    validators=[validate_phone_number], )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_('Avatar'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Is Staff'))
    last_login = models.DateTimeField(blank=True, null=True, verbose_name=_('Last Login'))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Joined'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    role = models.CharField(max_length=10, choices=[
        ('user', 'User'),
        ('admin', 'Admin'),
    ], verbose_name=_('Role'))

    def __str__(self):
        return self.user.username


class RSAInformation(models.Model):
    rsa_information_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='rsa_information')
    balance = models.FloatField(default=0, verbose_name=_('Balance'))
    role = models.CharField(max_length=50, choices=[
        ('client', 'Client'),
        ('mechanic', 'Mechanic'),
        ('tow_provider', 'Tow Provider'),
        ('taxi_driver', 'Taxi Driver'),
        ('quick_assistant_driver', 'Quick Assistant Driver'),
        ('admin', 'Admin'),
    ], verbose_name=_('Role'))
    rating = models.FloatField(default=0, verbose_name=_('Rating'))

    def __str__(self):
        return f"{self.user.username} - {self.role}"
