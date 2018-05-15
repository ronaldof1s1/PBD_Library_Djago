from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    name = models.CharField(unique=True)
    address = models.CharField()
    telephone = models.CharField()

    class Meta:
        abstract=True

    def __str__(self):
        return self.name

class Author(Person):
    CPF = models.CharField()
    pass

class Publisher(Person):
    CNPJ = models.CharField()

class Book(models.Model):
    name = models.CharField()
    keywords = models.TextField()
    quantity = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, related_name='books')

    def __str__(self):
        return self.name

class copy(models.Model):
    lent = models.BooleanField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')

    def __str__(self):
        if self.lent:
            lent = ' Emprestado'
        else:
            lent = ' Disponível'

        return self.book.name + lent
