from django.forms import ModelForm
from myapp.models import Sudent


class StudentForm(ModelForm):
    class Meta:
        model=Sudent
        fields="__all__"
