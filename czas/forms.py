import datetime 
import string
from django import forms
from .models import KontaktModel
from .models import CzasModel
from django.contrib.admin.widgets import AdminDateWidget







class KontaktmodelForm(forms.ModelForm):
    class Meta:
        model = KontaktModel
        fields = ['tytuł', 'email', 'treść', ]
        widgets = {'email': forms.EmailInput(attrs={'placeholder': 'Podaj Email.', 'class': 'form-control', 'rows': 1, 'column': 2}),
                   'tytuł': forms.Textarea(attrs={'placeholder': 'Tytuł Wiadomości.', 'class': 'form-control', 'rows': 1}),
                   'treść': forms.Textarea(attrs={'placeholder': 'Treść Wiadomości.', 'class': 'form-control', 'rows': 5})

                   }
        labels = {'email': (''), 'tytuł': (''), 'treść': (''), }
        # help_texts = {'email': ('Podaj Email.'), 'tytuł': ('Podaj Tytuł.'), 'treść': ('Napisz Wiadomość.'), }
        success_url = "/sukces/"

    # def clean_email(self, *args, **kwargs):
    #     lista_slow = ['dupa', 'huj', 'chuj', 'cipa', 'kurwa', 'gowno']
    #     lista_domen = ['onet.pl','gmail.com', 'interia.pl', 'wp.pl', 'o2.pl',' yahoo.com', 'hotmail.com']

    #     email = self.cleaned_data['email']
    #     for slowo in lista_slow:
    #         if slowo in str(email)[0:email.index("@")]:
    #             raise forms.ValidationError(f'Sam jesteś {str(email)[0:email.index("@")]}.')
    #     for i in string.punctuation:
    #         if i == "@" or i == ".":
    #             continue
    #         elif i in str(email):
    #             raise forms.ValidationError(f'W emailu {str(email)} znajdują się zakazane znaki.')



lata = list(range(datetime.datetime.now().year, 1802, -1))



class CzasModelForm(forms.ModelForm):

    class DateInput(forms.DateInput):
        input_type='date'


    data = forms.DateField(widget=DateInput)
    
    
    class Meta:
        model = CzasModel
        fields = ['imie', 'data']
        widgets = {'data': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'rows':'2', }), 
                  'imie': forms.TextInput(attrs={'placeholder': 'Podaj Imię.', 'class': 'form-control',})}

        labels = {'imie': ('Imię'), 'data': ('Data Ur:') }

    def clean_email(self, *args, **kwargs):
        lista_slow = ['dupa', 'huj', 'chuj', 'cipa', 'kurwa', 'gowno', 'pizda','ciota', 'debil']
        lista_domen = ['onet.pl','gmail.com', 'interia.pl', 'interia.eu', 'wp.pl', 'o2.pl',' yahoo.com', 'hotmail.com']

        email = self.cleaned_data['email']
        for slowo in lista_slow:
            if slowo in str(email)[0:email.index("@")].lower():
                raise forms.ValidationError(f'Sam jesteś {str(email)[0:email.index("@")]}.')
        for i in string.punctuation:
            if i == "@" or i == ".":
                continue
            elif i in str(email):
                raise forms.ValidationError(f'W emailu {str(email)} znajdują się zakazane znaki.')


        if str(email)[email.index("@")+1:] not in lista_domen:
            raise forms.ValidationError(f'Ta domena {str(email)[email.index("@")+1:]} jest zakazana.')
        else:
            return email
            
