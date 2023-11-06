from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    menu_name = models.CharField(max_length=200,default=0)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"