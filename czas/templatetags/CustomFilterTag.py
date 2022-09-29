import random
import string
from django import template


register = template.Library()


@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter(name='haslo')
def haslo(value):
    znaki = string.punctuation

    haslo_lic_zn = ""
    for t in value.split(" "):
            duza_litera = random.choice([t.upper(), t])
            haslo_lic_zn += "".join(duza_litera[0:3])
            haslo_lic_zn += str(random.randint(0, 10))
            haslo_lic_zn += random.choice(znaki)
    return haslo_lic_zn