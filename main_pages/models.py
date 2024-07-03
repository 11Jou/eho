from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.


current_year = datetime.date.today().year
    
class CSR(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title_en = models.CharField(max_length=500)
    content_en = models.TextField(max_length=5000)
    title_ar = models.CharField(max_length=500)
    content_ar = models.TextField(max_length=5000)
    cover = models.ImageField(upload_to='CSR/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural  = "CSR"


    def __str__(self) -> str:
        return self.name
    

class CSRImage(models.Model):
    related_CSR = models.ForeignKey(CSR, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='CSR/%Y/%m/%d/')


    
    class Meta:
        verbose_name_plural  = "CSR Images"


    def __str__(self) -> str:
        return str(self.related_CSR)


class Manager(models.Model):
    name = models.CharField(max_length=200)
    start_year = models.IntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(current_year)
        ]
    )

    end_year = models.IntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(current_year)
        ]
    )
    image = models.ImageField(upload_to='managers/%Y/%m/%d/', blank=True, null=True)

    def clean(self) -> None:
        super().clean()
        if self.end_year < self.start_year:
            raise ValidationError('End year must be greater than start year.')

    def __str__(self) -> str:
        return self.name