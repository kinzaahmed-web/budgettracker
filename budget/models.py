from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime


""" The models.py helps define the business objects and data structures. They are 'entities' of
the application which are persisted in the database.  """

# This is class that defines the certain fields or objects within a project
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project", null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def budget_expenses(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amt = 0
        for expense in expense_list:
            total_expense_amt += expense.amount
        return total_expense_amt
    
    def budget_remaining(self):
        total_expense_amt = self.budget_expenses()
        return self.budget - total_expense_amt

    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)

# This class defines the objects for the Categories
class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

# This class defines the objects for the Expenses
class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)