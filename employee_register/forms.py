from django import forms
from . models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        # this will retrieve all the fields available...
        #fields = '__all__'
        fields = ('full_name', 'emp_code', 'mobile', 'position')

    def __init__(self, *args, **kwargs): 
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"

        # This is just if you want any field not to make as required.. by default
        # it will be as required.
        self.fields['full_name'].required = False
        
