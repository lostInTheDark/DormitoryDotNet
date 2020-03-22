from django.db import models

class Dormitory(models.Model):
    Dormitory_number = models.IntegerField(max_length=2)
    Floor_amount = models.IntegerField(max_length=1)
    address = models.CharField(max_length=200)
    Amount_of_rooms = models.IntegerField(max_length=5)

    def __str__(self):
        return str(self.Dormitory_number)

    class Meta:
        verbose_name = 'Гуртожиток'
        verbose_name_plural = 'Гуртожитки'

class Floor(models.Model):
    Dormitory  = models.ForeignKey(Dormitory, on_delete = models.CASCADE)
    Floor_number = models.IntegerField(max_length=2)
    Number_of_rooms = models.IntegerField(max_length=5)

    def __str__(self):
        return str(self.Floor_number)

    class Meta:
        verbose_name = 'Поверх'
        verbose_name_plural = 'Поверхи'

class Room(models.Model):
    Floor = models.ForeignKey(Floor, on_delete = models.CASCADE)
    Room_number = models.IntegerField(max_length=5)
    Amount_of_places = models.IntegerField(max_length=1)

    def __str__(self):
        return str(self.Room_number)
    
    class Meta:
        verbose_name = 'Кімната'
        verbose_name_plural = 'Кімнати'
    
    