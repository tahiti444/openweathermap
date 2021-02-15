from django.db import models

# Create your models here.
class ResponseAPI(models.Model):
    time = models.DateTimeField()
    city = models.CharField(max_length=200)
    temp = models.DecimalField(max_digits=6, decimal_places=2)
    temp_min = models.DecimalField(max_digits=6, decimal_places=2)
    temp_max = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.city + " @ " + str(self.time)

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)