# from django.contrib import admin
# from carts.admin import CartTabAdmin
# from orders.admin import OrderTabulareAdmin

# from users.models import User

# # admin.site.register(User)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["username", "first_name", "last_name", "email",]
#     search_fields = ["username", "first_name", "last_name", "email",]

    

#     inlines = [CartTabAdmin, OrderTabulareAdmin]

from django.contrib import admin
from .models import User, Suggestion  # Импортируем модель Suggestion
from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name", "last_name", "email"]
    inlines = [CartTabAdmin, OrderTabulareAdmin]

# Регистрация модели Suggestion
@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'suggestion', 'created_at']
    search_fields = ['name', 'email', 'suggestion']
