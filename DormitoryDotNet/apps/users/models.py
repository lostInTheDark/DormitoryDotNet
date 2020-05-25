from django.db import models
from django.contrib.auth.models import User
from DormitoryManagement.models import Room



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    prof_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExists:
        pass
    else:
        instance.user.delete()

models.signals.post_delete.connect(delete_user, sender=Profile)
