from django import forms

class addtaskform(forms.Form):
    activity=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'task'}), max_length=100, required=True)

class edittaskform(forms.Form):
    activity=forms.CharField(label='', max_length=100, required=True)
    st=forms.BooleanField(label='',required=False)


class yearmonthform(forms.Form):
    mon = (('January','January'), ('February','February'), ('March','March'), ('April','April'), ('May','May'), ('June','June'), ('July','July'), ('August','August'), ('September','September'), ('October','October'), ('November','November'), ('December','December'))
    #m=forms.MultipleChoiceField(choices=mon, required=True)
    m=forms.ChoiceField(choices=mon)
    #m1=forms.CharField(label='', required=True)
    y=forms.IntegerField(label='',min_value=1950,max_value=2050)
     