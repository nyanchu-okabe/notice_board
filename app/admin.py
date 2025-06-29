# app/admin.py
from django.contrib import admin
from .models import Thread, Comment
from django import forms

class ThreadAdminForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    form = ThreadAdminForm
    list_display = ('thread_name', 'slug', 'password', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('thread_name', 'slug')

admin.site.register(Comment)
