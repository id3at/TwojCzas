
import random
import pickle
from django.shortcuts import render
from .forms import KontaktmodelForm, CzasModelForm
from django.views.generic import CreateView
from django.utils import timezone
from django import template
from .models import CzasModel
from .utils import get_plot, czaszycia2, cytaty

register = template.Library()


# Create your views here.

cytat = cytaty()
data = timezone.now
kolory = [random.randint(700000, 999999) for t in range(1, 100)]
dane = {"kolor": kolory, 'cytat':cytat, 'data': data}


class KontaktModelView(CreateView):
    template_name = 'kontakt.html'
    form_class = KontaktmodelForm
    success_url="/sukces/"

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**dane)
        context['cos'] = 'cos'

        return context

def sukces(request):
    return  render(request, "sukces.html", dane)

def get_name2(request):
    # username = request.META['USERNAME']
    obj = CzasModel.objects.all()
    wszystkie_lata = []
    for t in range(len(obj)):
        wszystkie_lata.append(int(str(obj[t].data)[0:4]))
    lata_x = list(set(wszystkie_lata))
    lata_x.pop(lata_x.index(2021))
    ilosc_y =[]
    for t in lata_x:
        ilosc_y.append(wszystkie_lata.count(t))
    
    chart = get_plot(lata_x, ilosc_y)
       
    if request.method == 'POST':

        
        form = CzasModelForm(request.POST or None)
        slownik = request.POST
        data_for = slownik['data'].split('-')
        twojczas = czaszycia2(IMIE=slownik['imie'], ROK=int(
            data_for[0]), MIESIAC=int(data_for[1]), DZIEN=int(data_for[2]))

        imie = twojczas[0]

        
        dane2 = {'form': form, "twojczas": twojczas,
                 "kolor": kolory, 'slownik': slownik, "chart": chart, "imie": str(imie), 'cytat':cytat, 'data':data,}
                 
        
        if form.is_valid():   
            form.save()

            CzasModelForm()
            return render(request, 'czas_policzony.html', context=dane2)

    
    else:
        form = CzasModelForm()
        dane2 = {'form': form, "kolor": kolory, "data": data, "chart": chart, 'cytat':cytat, 'data':data }

    return render(request, 'czas.html', context=dane2)


