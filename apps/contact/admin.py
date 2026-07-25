"""
Admin configuration for Contact app.
"""
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sector', 'created_at', 'is_read')
    list_filter = ('is_read', 'sector', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'sector', 'message', 'created_at')
    date_hierarchy = 'created_at'

    fieldsets = (
        (_('Expéditeur'), {
            'fields': ('name', 'email', 'phone', 'sector')
        }),
        (_('Message'), {
            'fields': ('subject', 'message')
        }),
        (_('Statut'), {
            'fields': ('is_read', 'created_at')
        }),
    )

    def has_add_permission(self, request):
        return False  # Submissions come from the form only
