from django.db import models

# Create your models here.
class ResponseAPI(models.Model):
    time = models.DateTimeField()
    city = models.CharField(max_length=200)
    temp = models.DecimalField(max_digits=6, decimal_places=2)
    temp_min = models.DecimalField(max_digits=6, decimal_places=2)
    temp_max = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.city + " @ " + str(self.time)
