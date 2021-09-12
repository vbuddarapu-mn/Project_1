from django import forms
from .models import generalReminder

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class MyForm(forms.ModelForm):
    class Meta:
        model = generalReminder
        widgets = {
            'reminder_date': DateInput(),
            'reminder_time': TimeInput(),
        }
        fields = ["reminder_name","reminder_desc", "reminder_date","reminder_time",'reminder_prenotice',"reminder_replay"]
        labels = {'reminder_name': "Title", "reminder_desc": "Description","reminder_date":"Date","reminder_time":"Time","reminder_replay":"Replay","reminder_prenotice":"Prenotice period"}