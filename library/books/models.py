from turtle import title
from uuid import uuid4
from venv import create
from django.db import models

# Create your models here.
class Books(models.Model):
    id_book = models.UUIDField(primary_key=True,default=uuid4, editable=False) #Setamos que é a PK, modelo uuid4 importado, e não pode ser editado
    title = models.CharField(max_length=255) #Campo de texto com max de 255 caracteres
    author = models.CharField(max_length=255) #Campo de texto com max de 255 caracteres
    release_year = models.IntegerField() #Campo de inteiro
    state = models.CharField(max_length=50) #Campo de texto com max de 50 caracteres
    pages = models.IntegerField() #Campo de inteiro
    publishing_company = models.CharField(max_length=255) #Campo de texto com max de 255 caracteres
    create_at = models.DateField(auto_now_add=True) #Campo de data, que é adicionado automaticamente