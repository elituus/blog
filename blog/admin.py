from django.contrib import admin
from .models import Post

#nombre  dajngogirls/admin.py
#Registra nuestro objeto post  en el administrador 
#de django  para  poder consultar  o actualizar la informacion
#del o de los post
admin.site.register(Post)
