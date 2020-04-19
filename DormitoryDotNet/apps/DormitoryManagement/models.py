from django.db import models


class Dormitory(models.Model):
    Dormitory_number = models.IntegerField()
    Floor_amount = models.IntegerField()
    address = models.CharField(max_length=200)
    Amount_of_rooms = models.IntegerField()

    def __str__(self):
        return str(self.Dormitory_number)

    class Meta:
        verbose_name = 'Dormitory'
        verbose_name_plural = 'Dormitories'


class Floor(models.Model):
    Dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    Floor_number = models.IntegerField()
    Number_of_rooms = models.IntegerField()

    def __str__(self):
        return str(self.Floor_number)

    class Meta:
        verbose_name = 'Floor'
        verbose_name_plural = 'Floors'


class Room(models.Model):
    Floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    Room_number = models.IntegerField()
    Amount_of_places = models.IntegerField()

    def __str__(self):
        return str(self.Room_number)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
