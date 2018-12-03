from django.db import models


class Farmer(models.Model):
    # farmer's bio
    ordering = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    membership_number = models.CharField(max_length=255, unique=True)
    id_number = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)

    # bank details
    bank = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('ordering', )


class Employee(models.Model):
    # employee's bio
    ordering = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    monthly_salary = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    # bank details
    bank = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('ordering', )


class Delivery(models.Model):
    # delivery stats
    date = models.DateField(null=True, blank=True)
    farmer = models.CharField(max_length=255)
    kilograms = models.CharField(max_length=255)
    rate = models.CharField(max_length=255, default=35)
    amount = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Deliveries"


class Expenditure(models.Model):
    # expenditure stats
    date = models.DateField(null=True, blank=True)
    amount = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Expenditure"


class MonthlyTotal(models.Model):
    # monthly stats
    month = models.CharField(max_length=255)
    farmer = models.CharField(max_length=255)
    total_kilograms = models.CharField(max_length=255)
    rate = models.CharField(max_length=255, default=35)
    total_amount = models.CharField(max_length=255)
    prev_loan_balance = models.CharField(max_length=255, null=True, blank=True)
    vet_loans = models.CharField(max_length=255, null=True, blank=True)
    advance = models.CharField(max_length=255, null=True, blank=True)
    store_loans = models.CharField(max_length=255, null=True, blank=True)
    total_loans = models.CharField(max_length=255, null=True, blank=True)
    total_deductions = models.CharField(max_length=255, null=True, blank=True)
    net_pay = models.CharField(max_length=255, null=True, blank=True)
    loan_balance = models.CharField(max_length=255, null=True, blank=True)


class FarmerAnalytics(models.Model):
    # farmer analytics
    farmer_name = models.CharField(max_length=255)
    total_delivery_days = models.CharField(max_length=255)
    total_kilograms = models.CharField(max_length=255)
    total_pay = models.CharField(max_length=255)
    average_monthly_kilograms = models.CharField(max_length=255)
    average_monthly_pay = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Farmer Analytics"


class MonthlyBusinessReport(models.Model):
    # monthly business stats
    month = models.CharField(max_length=255)
    total_payments = models.CharField(max_length=255)
    total_salaries = models.CharField(max_length=255)
    total_expenditure = models.CharField(max_length=255)
    profit_or_loss = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Monthly Business Reports"
