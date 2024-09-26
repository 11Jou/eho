from django import template

register = template.Library()

@register.filter
def custom_replace(value, args):
    """
    Custom replace filter that replaces the first string with the second one.
    Usage: {{ value|custom_replace:"old,new" }}
    """
    old, new = args.split(',')
    return value.replace(old, new)
