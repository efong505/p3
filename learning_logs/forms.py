from django import forms

from .models import Topic, Entry, BreakEvenPoint

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
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
        
class BreakEvenPointForm(forms.ModelForm):
    class Meta:
        model = BreakEvenPoint
        fields =['fixed_cost', 'reg_price', 'disc_price']
        labels = {'fixed_cost':'Fixed Cost'}