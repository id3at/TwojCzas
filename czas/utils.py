import matplotlib.pyplot as plt
import matplotlib
import base64
import datetime
import requests
import random
import numpy as np
import pickle
import os
from django.conf import settings
from io import BytesIO
from bs4 import BeautifulSoup




def cytaty():
    file_path = os.path.join(settings.STATIC_ROOT, 'cytaty')
    infile = open(file_path,'rb')
    lista_cytatow = pickle.load(infile)
    infile.close()
    lista_cytatow_np = np.array(lista_cytatow).reshape(int(len(lista_cytatow)/2),2 )
  
    return lista_cytatow_np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, transparent=True, format="png",)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):
    matplotlib.use("Agg")
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))

    plt.style.use('dark_background')
    matplotlib.rc('axes',edgecolor='#dc3545')
    plt.bar(x, y, color="#dc3545")
    plt.xlim(1960,2019)

   
    plt.title("Statystyka", color="#dc3545")
    plt.xlabel('Lata', color="#dc3545")
    plt.ylabel('Ilość wykonanych obliczeń', color="#dc3545")
    plt.tight_layout()
    graph = get_graph()
    return graph

def czaszycia2(IMIE, ROK, MIESIAC, DZIEN):

    AKTUALNYCZAS = datetime.datetime.today()
    DATANARODZIN = datetime.datetime(ROK, MIESIAC, DZIEN)
    urojony = datetime.datetime((AKTUALNYCZAS.year+1), MIESIAC, DZIEN)
    Wiek = AKTUALNYCZAS.year - DATANARODZIN.year
    mies = AKTUALNYCZAS.month - DATANARODZIN.month
    kiedysto = 100 + DATANARODZIN.year
    Wiekdelta = AKTUALNYCZAS - DATANARODZIN
    sek = Wiekdelta.total_seconds()
    min = sek / 60
    godziny = min / 60
    przyszleur = urojony - AKTUALNYCZAS
    za_ile_dni_ur = przyszleur.days
    ile_tygodni = Wiekdelta.days // 7
    resztatygodni = (Wiekdelta.days - ((Wiekdelta.days // 7) * 7))
    AKTUALNYCZAS_format = f'{AKTUALNYCZAS:%d, %m, %Y, %H:%M:%S}'
    if mies < 0:
        mies = 12 + int(mies)
        Wiek = int(AKTUALNYCZAS.year - DATANARODZIN.year) - 1
    if za_ile_dni_ur > 364:
        za_ile_dni_ur -= 364

    wiekmies = (Wiek) * 12 + (mies)

    odmiana_miesiecy = ""

    if str(mies) == "1":
        odmiana_miesiecy = "miesiąc"
    elif str(mies)[-1] == "2" or str(mies)[-1] == "3" or str(mies)[-1] == "4":
        odmiana_miesiecy = "miesiące"
    else:
        odmiana_miesiecy = "miesięcy"

    odmiana_miesiecy_suma = ""
    if str(wiekmies) == "1":
        odmiana_miesiecy_suma = "miesiąc"
    elif str(wiekmies)[-1] == "2" or str(wiekmies)[-1] == "3" or str(wiekmies)[-1] == "4":
        odmiana_miesiecy_suma = "miesiące"
    else:
        odmiana_miesiecy_suma = "miesięcy"

    odmiana_tygodni = ""
    if str(ile_tygodni) == "0":
        odmiana_tygodni = "tygodni"
    elif str(ile_tygodni) == "1":
        odmiana_tygodni = "tydzień"
    elif str(ile_tygodni) == "2" or str(ile_tygodni) == "3" or str(ile_tygodni) == "4":
        odmiana_tygodni = "tygodnie"
    else:
        odmiana_tygodni = "tygodni"

    odmiana_dni= ""
    if str(Wiekdelta.days) == "1":
        odmiana_dni = "dzień"
    else:
        odmiana_dni = "dni"

    dzien_tygodnia =""
    if AKTUALNYCZAS.strftime("%A") == "Monday":
        dzien_tygodnia = 'Poniedziałek'
    elif AKTUALNYCZAS.strftime("%A") == "Tuesday":
        dzien_tygodnia = 'Wtorek'
    elif AKTUALNYCZAS.strftime("%A") == "Wednesday":
        dzien_tygodnia = 'Środa'
    elif AKTUALNYCZAS.strftime("%A") == "Thursday":
        dzien_tygodnia = 'Czwartek'
    elif AKTUALNYCZAS.strftime("%A") == "Friday ":
        dzien_tygodnia = 'Piątek'
    elif AKTUALNYCZAS.strftime("%A") == "Saturday":
        dzien_tygodnia = 'Sobota'
    elif AKTUALNYCZAS.strftime("%A") == "Sunday":
        dzien_tygodnia = 'Niedziela'

    c = (f"""\n Witaj, {IMIE} !! \n
    Jest: {dzien_tygodnia} {AKTUALNYCZAS:%d, %m, %Y, %H:%M:%S}.
    Masz: {Wiek} lat i {mies} {odmiana_miesiecy}.
    Przeżyłeś już: {wiekmies:,} {odmiana_miesiecy_suma}
    a to jest: {ile_tygodni} {odmiana_tygodni} i {resztatygodni} {odmiana_dni},
    czyli {Wiekdelta.days:,} {odmiana_dni},
    a to jest: {int(godziny):,} godzin,
    a to jest: {int(min):,} minut,
    a to jest: {int(sek):,} sekund.
    100 lat osiągniesz w roku:, {kiedysto}
    Urodziny obchodzisz za {int(za_ile_dni_ur)} dni ;)""")
    
    return IMIE, dzien_tygodnia, AKTUALNYCZAS_format, Wiek, mies, odmiana_miesiecy, wiekmies, odmiana_miesiecy_suma, ile_tygodni, odmiana_tygodni, resztatygodni, odmiana_dni, Wiekdelta.days, int(godziny), int(min), int(sek), kiedysto, za_ile_dni_ur