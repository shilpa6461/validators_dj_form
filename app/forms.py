from django import forms

def Validate_for_a(Svalue):
    if Svalue[0]=='a':
        raise forms.ValidationError('First letter should not be a')

def Validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('len is lessthan 5')


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[Validate_for_a,Validate_for_len])
    Sage=forms.IntegerField()
    email=forms.EmailField(validators=[Validate_for_a])