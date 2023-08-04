from django.contrib import admin
from .models import Pessoa

# Aqui registramos nossos models. Para iniciar, primeiro crie um superuser com o comando 'python manage.py createsuperuser'.
admin.site.register(Pessoa)  # Cria o formulário dentro da área administrativa para a model.
