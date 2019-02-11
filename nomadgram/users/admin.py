from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from nomadgram.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

class UserInlineAdmin(admin.TabularInline):
    model = User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        ("User", {"fields": ("name","followers","following","profile_image"
        )}),
    ) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
    
