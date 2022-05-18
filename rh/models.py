from django.db import models

# Create your models here.

class Empresa (models.Model):
    Nome = models.CharField(max_length=255)

def __str__(self):
        return self.nome

class Area (models.Model):
    Cargos = models.CharField(max_length=255)
    Departamento = models.CharField(max_length=255)
    Empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} - Dep: {self.departamento.nome}'


class Colaboradores (models.Model):
	Nome = models.CharField(max_length=255)
	Salario = models.DecimalField(decimal_places=2, max_digits=10)
	Horas_Extra = models.DecimalField(decimal_places=1, max_digits=4)
Cargo = models.ForeignKey(Area, on_delete=models.PROTECT)

def __str__(self):
        return self.nome

class Ponto (models.Model):
    Colaborador = models.ForeignKey(Colaboradores, on_delete=models.DO_NOTHING)
    Carga_Horaria = models.DecimalField(decimal_places=2, max_digits=10)
    Entrada = models.DateTimeField()
    Saida = models.DateTimeField()

    def __str__(self):
        return f'Colab {self.Colaborador} - {self.Entrada} :: {self.Saida} / {self.Carga_Horaria}'

class Notas (models.Model):
	Numero = models.DecimalField(decimal_places=2, max_digits=100)
Data = models.DateField()
Fornecedor = models.ForeignKey(Empresa, on_delete=models.CASCADE)
Cliente = models.CharField(max_length=255)
Imposto = models.DecimalField(decimal_places=2, max_digits=10)
Valor_Nota = models.DecimalField(decimal_places=2, max_digits=100)

def __str__(self):
        return f'Nota {self.Numero} : {self.Data} : {self.Valor_Nota}'

class Contabilidade (models.Model):
    Nome = models.ForeignKey(Empresa, on_delete=models.PROTECT)
Saldo = models.DecimalField(decimal_places=2, max_digits=100)
Despesas = models.DecimalField(decimal_places=2, max_digits=100)
Salarios = models.DecimalField(decimal_places=2, max_digits=100)
Arrecadação = models.DecimalField(decimal_places=2, max_digits=100)

def __str__(self):
        return self.Nome





