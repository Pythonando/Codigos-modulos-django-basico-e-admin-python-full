from django import template

register = template.Library()

@register.filter(name='teste')
def teste(v1):
    if v1 == 12:
        return f'usuario master do sistema {v1}'
    else:
        return v1