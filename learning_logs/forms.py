from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # overriding the Django's default widget choices.

# In Django:
# class Meta; an inner(nested) class contains Metadata,
# Metadata; a set of data describes and gives information about other data. 