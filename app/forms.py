# app/forms.py
from django import forms
from .models import Thread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread_name', 'slug', 'password']  # 'title' を 'thread_name' に変更
        widgets = {
            'thread_name': forms.TextInput(attrs={'placeholder': 'スレッドの名前を入力'}),
            'slug': forms.TextInput(attrs={'placeholder': 'スレッドのスラッグを入力'}),
            'password': forms.TextInput(attrs={'placeholder': 'スレッドのパスを入力'}),
        }
