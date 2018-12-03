from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import (
    Farmer, Employee, Delivery, Expenditure, MonthlyTotal, FarmerAnalytics, MonthlyBusinessReport
)


class FarmerModel(admin.ModelAdmin):
    list_display = (
        'ordering',
        'name',
        'membership_number',
        'id_number',
        'phone',
        'active',
    )
    list_filter = (
        'active',
    )
    list_display_links = ('name', 'membership_number')
    list_editable = (
        'ordering',
        'active',
    )
    search_fields = ('name', 'membership_number', 'id_number', 'phone', 'email',)

    fieldsets = (
        ('FARMER\'S BIO', {
            'fields': ('ordering', 'name', 'membership_number', 'id_number', 'phone', 'email', 'active')
        }),
        ('BANK DETAILS', {
            'fields': ('bank', 'branch', 'account_number')
        }),
    )


class EmployeeModel(admin.ModelAdmin):
    list_display = (
        'ordering',
        'name',
        'id_number',
        'phone',
        'active',
    )
    list_filter = ('active', )
    list_display_links = ('name',)
    list_editable = ('active',)
    search_fields = (
        'name',
        'id_number',
        'phone',
        'email',
    )

    fieldsets = (
        ('EMPLOYEE\'S BIO', {
            'fields': ('ordering', 'name', 'id_number',
                       'phone', 'email', 'monthly_salary', 'active')
        }),
        ('BANK DETAILS', {
            'fields': ('bank', 'branch', 'account_number')
        }),
    )


class DeliveryModel(admin.ModelAdmin):
    list_display = (
        'date',
        'farmer',
        'kilograms',
        'rate',
        'amount',
    )
    list_display_links = ('date', 'farmer')
    search_fields = (
        'date',
        'farmer',
        'kilograms',
        'rate',
        'amount',
    )

    fieldsets = (('DELIVERY DETAILS', {
        'fields': (
            'date',
            'farmer',
            'kilograms',
            'rate',
            'amount',
        )
    }), )


class ExpenditureModel(admin.ModelAdmin):
    list_display = (
        'date',
        'amount',
        'description',
    )
    list_display_links = ('date', 'amount')
    search_fields = (
        'date',
        'amount',
        'description',
    )

    fieldsets = (('EXPENDITURE DETAILS', {
        'fields': (
            'date',
            'amount',
            'description',
        )
    }), )
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 4,
                'cols': 100
            })
        }
    }


class MonthlyTotalModel(admin.ModelAdmin):
    list_display = (
        'month',
        'farmer',
        'total_kilograms',
        'total_amount',
        'total_deductions',
        'net_pay',
        'loan_balance',
    )
    list_display_links = ('month', 'farmer')
    search_fields = (
        'month',
        'farmer',
    )

    fieldsets = (('MONTHLY TOTALS DETAILS', {
        'fields': (
            'month',
            'farmer',
            'total_kilograms',
            'rate',
            'total_amount',
            'prev_loan_balance',
            'vet_loans',
            'advance',
            'store_loans',
            'total_loans',
            'total_deductions',
            'net_pay',
            'loan_balance',
        )
    }), )


class FarmerAnalyticsModel(admin.ModelAdmin):
    list_display = (
        'farmer_name',
        'total_delivery_days',
        'total_kilograms',
        'total_pay',
        'average_monthly_kilograms',
        'average_monthly_pay',
    )
    list_display_links = ('farmer_name',)
    search_fields = (
        'farmer_name',
    )

    fieldsets = (('FARMER ANALYTICS DETAILS', {
        'fields': (
            'farmer_name',
            'total_delivery_days',
            'total_kilograms',
            'total_pay',
            'average_monthly_kilograms',
            'average_monthly_pay',
        )
    }), )


class MonthlyBusinessReportModel(admin.ModelAdmin):
    list_display = (
        'month',
        'total_payments',
        'total_salaries',
        'total_expenditure',
        'profit_or_loss',
    )
    list_display_links = ('month',)
    search_fields = ('month', )

    fieldsets = (('MONTHLY REPORT DETAILS', {
        'fields': (
            'month',
            'total_payments',
            'total_salaries',
            'total_expenditure',
            'profit_or_loss',
        )
    }), )


admin.site.register(Farmer, FarmerModel)
admin.site.register(Employee, EmployeeModel)
admin.site.register(Delivery, DeliveryModel)
admin.site.register(Expenditure, ExpenditureModel)
admin.site.register(MonthlyTotal, MonthlyTotalModel)
admin.site.register(FarmerAnalytics, FarmerAnalyticsModel)
admin.site.register(MonthlyBusinessReport, MonthlyBusinessReportModel)
