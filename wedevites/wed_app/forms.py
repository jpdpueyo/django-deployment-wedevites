from django import forms
from wed_app.models import Guest
from django.contrib.auth import(authenticate,get_user_model,login)


User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        user = authenticate(username = username)
        if not user:
            raise forms.ValidationError('This user does not exist')
        return super(UserLoginForm, self).clean(*args,**kwargs)

class RSVPForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs = {'class':"form-control",'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs = {'class':"form-control test",'placeholder': 'Email'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control test", 'placeholder': 'Mobile Number'}))
    class Meta:
        model = Guest
        # fields = '__all__'
        fields = ['name','email','number','status']
        widgets = {'status': forms.RadioSelect(attrs={'class': 'montfont'})}
