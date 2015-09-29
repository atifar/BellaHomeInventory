from django.contrib import admin

from .models import CsCartCategory, CsCartSubcategory, CsCartProduct

admin.site.register(CsCartCategory)
admin.site.register(CsCartSubcategory)
admin.site.register(CsCartProduct)
