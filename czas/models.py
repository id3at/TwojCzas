from django.db import models

# Create your models here.



class KontaktModel(models.Model):
    tytuł = models.CharField(max_length=200)
    email = models.EmailField()
    treść = models.TextField()
    data_wpisu = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return '/kontakt'


class CzasModel(models.Model):
    email = models.EmailField()
    imie = models.CharField(max_length=20,)
    data = models.DateField()
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    # def clean_data(self, *args, **kwargs):
    #     data = self.cleaned_data['data']
    #     if ValueError:
    #         raise forms.ValidationError(f'"Zle", {data.day}')
    #     else:
    #         return data
