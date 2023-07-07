from django import forms

from newapp.models import task, details




class dateinput(forms.DateInput):
    input_type = "date"

class taskform(forms.ModelForm):
    DueDate = forms.DateField(widget=dateinput)
    class Meta:
        model = task
        fields=("__all__")


class detailform(forms.ModelForm):
    class Meta:
        model =details
        fields = ("__all__")