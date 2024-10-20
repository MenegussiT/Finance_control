from django.contrib import admin
from finance.models import User, Expense, ExpenseCategory, Revenue, RevenueCategory

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','surname','email')
    search_fields = ('name', 'surname', 'email')
    list_filter = ('name', 'surname', 'email')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('email')