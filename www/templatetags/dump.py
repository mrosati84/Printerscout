from django import template
import pprint

register = template.Library()

def dump(value):
    """
    template filter: use it like {{ var_name | dump }}. make sure you have
    {% load dump %} in your template
    """
    return pprint.pformat(vars(value), indent=4)

register.filter('dump', dump)
