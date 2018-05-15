from django.db import models
from django.utils import timezone
# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    neighborhood = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)


class Person(models.Model):
    name = models.CharField(unique=True, max_length=100)
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
    telephone = models.CharField(max_length=20)

    class Meta:
        abstract=True

    def __str__(self):
        return self.name

class Author(Person):
    CPF = models.CharField(max_length=14, unique=True)
    pass

class Publisher(Person):
    CNPJ = models.CharField(max_length=18, unique=True)

class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    keywords = models.TextField(max_length=100)
    quantity = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, related_name='books')

    def __str__(self):
        return self.name

class Copy(models.Model):
    lent = models.BooleanField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')

    def __str__(self):
        if self.lent:
            lent = ' Emprestado'
        else:
            lent = ' Disponível'

        return self.book.name + lent

class User(Person):
    student = models.BooleanField()

class Loan(models.Model):
    loan_date = models.DateField(default=timezone.now())
    return_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)


    def __str__(self):
        self.copy.__str__() + " -> " + self.user.__str__()