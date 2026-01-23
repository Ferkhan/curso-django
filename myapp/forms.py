from django import forms

class CreateTaskForm(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=100)
    description = forms.CharField(label="Descripción a realizar", widget=forms.Textarea, required = False)