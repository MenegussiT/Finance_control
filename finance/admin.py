from django.contrib import admin
from finance.models import User, Expense, ExpenseCategory, Revenue, RevenueCategory

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email']  
    search_fields = ['name', 'surname', 'email']  
    list_filter = ['name', 'surname', 'email'] 

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['email', 'category', 'description', 'value', 'expense_date', 'created_at']  
    search_fields = ['email'] 
    list_filter = ['email']  

class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  
    list_filter = ['name']  
    search_fields = ['name']  

class RevenueAdmin(admin.ModelAdmin):
    list_display = ['email', 'wage', 'varible_gain'] 
    list_filter = ['email']  
    search_fields = ['email']  

class RevenueCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  
    list_filter = ['name']  
    search_fields = ['name']  

# Registrar os modelos no admin
admin.site.register(User, UserAdmin)
admin.site.register(Expense, ExpenseAdmin)  
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Revenue, RevenueAdmin)
admin.site.register(RevenueCategory, RevenueCategoryAdmin)
