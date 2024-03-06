from django.db import models

# Create your models here.

class Habitacion (models.Model):
    
    nombre = models.CharField(max_length = 60)
    camas = models.IntegerField()
    
    def __str__ (self):
        
        return f"habitacion tipo {self.nombre}."

class Huesped (models.Model):
    
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 60)
    correo = models.EmailField()
    
    def __str__(self):
        
        return f"{self.nombre} --- {self.apellido}."
    
class Reserva (models.Model):
    
    checkin = models.DateField()
    checkout = models.DateField()
    
    def __str__(self):
        
        return f"reserva con igreso el {self.checkin}."