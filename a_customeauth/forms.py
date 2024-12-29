from django import forms

from a_customeauth.models import Profile

def getInputWidget(type:str,class_add=""):

    base_classes ="p-1 focus:border-black w-full border-2  rounded-lg " +class_add  

    inputs = {
        'text': forms.TextInput( {
            'required':False,
            "class":base_classes
        }),
        'email':forms.EmailInput({
            "class":base_classes
        }),
        'file':forms.FileInput({
            "class":base_classes
        })
    }

   
    return inputs[type]

class ProfileUpdateForm(forms.Form):
    avatar = forms.ImageField(
        show_hidden_initial=True,
        required=False,
        widget=getInputWidget('file'))
    username = forms.CharField(
        widget=getInputWidget('text')
    )
    email = forms.EmailField(
        widget=getInputWidget('email',class_add='col-span-2'))

    first_name = forms.CharField(
        required=False,
        widget=getInputWidget('text')
    )
    last_name = forms.CharField(
        required=False,
        widget=getInputWidget('text')
    )

