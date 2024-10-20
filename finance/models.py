from django.db import models


class user (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class expense_category (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class expense (models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(user, on_delete=models.CASCADE)
    category = models.ForeignKey(expense_category, on_delete=models.CASCADE)
    description = models.CharField(max_length=180)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class revenue (models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(user, on_delete=models.CASCADE)
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    varible_gain = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    

class revenue_category (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
