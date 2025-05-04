from django.contrib import admin

from .models import Checkout
admin.site.register(Checkout)
admin.site.site_header = "admin loc va dung"
