from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CreditCardProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CreditCardProfileInline(admin.TabularInline):
    model = CreditCardProfile
    extra = 0


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'role', 'is_active']
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_joined', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'role', 'is_staff', 'is_superuser', 'is_active')}
         ),
    )
    ordering = ('email',)
    inlines = (CreditCardProfileInline,)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CreditCardProfile)

