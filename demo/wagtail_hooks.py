from django.core.urlresolvers import reverse

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.menu import MenuItem


# @hooks.register('register_admin_menu_item')
# def register_frank_menu_item():
#     return MenuItem('Frank', reverse('kontakt'), classnames='icon icon-folder-inverse', order=10000)
