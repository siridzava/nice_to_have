from django import template


register = template.Library()


#@register.filter(name='cutt')
def steal(value, arg):
    return value.replace(arg, 'O')


register.filter('cutt', steal)
