from django import template
from menuapp.models import Menu

register = template.Library()

@register.inclusion_tag('menuapp/menu.html')
def draw_menu(menu_name, current_url):
    menu_items = Menu.objects.filter(menu_name=menu_name)
    for item in menu_items:
        if item.url == current_url:
            item.is_active = True
        else:
            item.is_active = False
    return {'menu_items': menu_items}