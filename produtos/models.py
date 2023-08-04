from django.db import models


# Aqui criamos classes que representarão nossas tabelas no banco de dados. 
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
# Para aplicar o modelo, usamos dois comandos no terminal: 'python manage.py makemigrations' para criar a modificação e 'python manage.py migrate' para aplicá-la.
 