from django.contrib import admin
from .models import Report, ReportField, ReportFindings

class ReportFindingsInline(admin.StackedInline):
    model = ReportFindings
    extra = 0

class ReportFieldInline(admin.StackedInline):
    model = ReportField
    extra = 0

class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "id",
                    "user",
                    "title",
                    "pub_date",
                    "return_date"
                ]
            },
        )
    ]

    readonly_fields = ("id",)

    inlines = [ReportFieldInline, ReportFindingsInline]

    save_as = True

admin.site.register(Report, ReportAdmin)
