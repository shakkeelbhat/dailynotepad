from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    title = forms.CharField(initial='Enter title here', widget=forms.TextInput(attrs={'placeholder': 'Enter title here'}))
    description = forms.CharField(initial='Enter description here', widget=forms.Textarea(attrs={'placeholder': 'Enter description here'}))
    completed = forms.BooleanField(required=False)
    due_date = forms.DateField(initial='yyyy-mm-dd', widget=DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']
