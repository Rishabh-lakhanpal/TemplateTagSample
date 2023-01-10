from django import template
from projectApp.models import YourModel
register = template.Library()

@register.filter()
def any_function(slot):
    return YourModel.objects.count()



# register = template.Library()

# from .models import YourModel
  
# @register.simple_tag
# def any_function():
#     return YourModel.objects.count()