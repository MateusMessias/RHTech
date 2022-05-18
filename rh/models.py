from django.db import models

# Create your models here.

class Empresa (models.Model):
    Nome = models.CharField(max_length=255)
Areas = models.CharField(max_length=255),
Balanço_Financeiro = models.DecimalField(decimal_places=2, max_digits=100),
Despesas = models.DecimalField(decimal_places=2, max_digits=100)
Salarios = models.DecimalField(decimal_places=2, max_digits=100)
    
def __str__(self):
        return self.nome

class Colaboradores (models.Model):
	Nome = models.CharField(max_length=255)
	Empresa = models.CharField(max_length=255)
	Pagamento_Mês = models.DecimalField(decimal_places=2, max_digits=10)
	Horas_Extra = models.DecimalField(decimal_places=1, max_digits=4)
	Cargo =  models.ForeignKey(Area, on_delete=models.CASCADE)
	
class Area (models.Model):
	Cargos = models.CharField(max_length=255)
	Area = models.CharField(max_length=255)
Empresa = models.ForeignKey(Area, on_delete=models.CASCADE)

class Contabilidade (models.Model):
	Empresa = models.ForeignKey(Area, on_delete=models.CASCADE)
Saldo = models.DecimalField(decimal_places=2, max_digits=100)
Despesas = models.DecimalField(decimal_places=2, max_digits=100)
Salarios = models.DecimalField(decimal_places=2, max_digits=100)
Arrecadação = models.DecimalField(decimal_places=2, max_digits=100)

class Nostas (models.Model):
	Numero = models.DecimalField(decimal_places=2, max_digits=100)
Data = models.DateField()
Empresa = models.ForeignKey(Contabilidade, on_delete=models.CASCADE)
Cliente = models.CharField(max_length=255)
Imposto = models.DecimalField(decimal_places=2, max_digits=10)
Valor = models.DecimalField(decimal_places=2, max_digits=100)

