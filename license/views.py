from django.shortcuts import render
from .models import generalReminder
from .form import MyForm
from datetime import date
from dateutil.relativedelta import relativedelta
# Create your views here.
def addDate(request):
    return render(request, 'license/base.html')

def my_form(request):
    if request.method == "POST":
      form = MyForm(request.POST)
      if form.is_valid():
          form.save()
    else:
      form = MyForm()
    data = generalReminder.objects.all()
    # data.license_add = data.license_date + relativedelta(months=+data.license_add)
    lic = {
        'reminder_list' :data
    }
    return render(request, 'license/base.html', {'form': form})

