from django import forms
class weightform(forms.Form):
    firstname=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':'FirstName'}))
    lastname = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':'LastName'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Age (In Years)'}))
    heightfeet = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Feet Height(in Feet)'}))
    heightinches = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Inches Height (In Inches)'}))