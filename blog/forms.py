from django import forms

from .models import Play, Submission

class PlayForm(forms.ModelForm):

    class Meta:
   	model = Play
        fields = ('title','play','counter',)

class ContactForm(forms.ModelForm):

    class Meta:
   	model = Submission
        fields = ('submitter','contact','message',)
	widgets = {
            'submitter': forms.TextInput(attrs={'placeholder': 'NAME'}),
            'contact': forms.TextInput(attrs={'placeholder': 'EMAIL'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'GIVE US IDEAS  /  TELL US HOW TERRIBLE WE REALLY ARE'}),
        }

