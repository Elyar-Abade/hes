from django.contrib import admin
from .models import Item, Comment, Reaction

# Register your models here.
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Reaction)