from django import forms

from .models import MessageContact


class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Écrivez votre message ici...'}),
            'sujet': forms.TextInput(attrs={'placeholder': 'Objet de votre message'}),
            'nom': forms.TextInput(attrs={'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Votre email'}),
        }
