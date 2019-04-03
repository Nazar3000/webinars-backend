import uuid
from timezone_field import TimeZoneField

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('admin', 'admin'),
        ('trial', 'trial'),
        ('tariff', 'tariff')
    )

    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Is the user allowed to have access to the admin',
    )
    is_active = models.BooleanField(
        'active',
        default=False,
        help_text='Is the user account currently active',
    )
    role = models.CharField(choices=ROLES, max_length=6, default='trial')

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
        null=True,
        blank=True
    )
    avatar = models.ImageField(blank=True, null=True, upload_to='user_profiles/avatars')
    timezone = TimeZoneField(default='Europe/London')

    bot_id = models.UUIDField(default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        if self.is_staff:
            self.role = 'admin'
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.email)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class DeviceData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    user_agent = models.CharField(max_length=2048)
    ip_address = models.GenericIPAddressField()
    last_activity = models.DateTimeField()
    country = models.CharField(max_length=64, default='United Kingdom')
    region = models.CharField(max_length=64, default='London')

    class Meta:
        verbose_name = "Device Data"
        verbose_name_plural = "Device Data instances"

    def __str__(self):
        return '{}: {}'.format(self.country, self.region)


class CreditCardProfile(models.Model):
    cc_number = models.CharField(max_length=16,
                                 validators=(RegexValidator(r'^\d{13,16}$'),),
                                 verbose_name='cardholder number'
                                 )
    cc_name = models.CharField(max_length=256, verbose_name='cardholder name')
    cc_expiry_date = models.DateField(verbose_name='expiry date MM/YYYY')
    cvv_code = models.PositiveIntegerField(validators=(MinValueValidator(100),
                                                       MaxValueValidator(9999)),
                                           verbose_name='CVV code'
                                           )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Credit Card Profile"
        verbose_name_plural = "Credit Card Profiles"

    def __str__(self):
        return '{}-{}'.format(self.cc_number, self.user)
