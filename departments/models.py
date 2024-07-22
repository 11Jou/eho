from django.db import models

# Create your models here.


class QHSEMainContent(models.Model):
    title_en = models.CharField(max_length=100,)
    content_en = models.TextField(max_length=3000, null=True, blank=True)
    title_ar = models.CharField(max_length=100)
    content_ar = models.TextField(max_length=3000, null=True, blank=True)

    
    class Meta:
        verbose_name_plural  = "HSE Main Content"



    def __str__(self) -> str:
        return self.title_en


class QHSEContent(models.Model):
    related_title = models.ForeignKey(QHSEMainContent, on_delete=models.CASCADE)
    content_en = models.TextField(max_length=3000)
    content_ar = models.TextField(max_length=3000)


    class Meta:
        verbose_name_plural  = "HSE Content"


    def __str__(self) -> str:
        return str(self.related_title)





class QHSEPDF(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='HSE PDF/%Y/%m/%d/')



    class Meta:
        verbose_name_plural  = "HSE PDF"



    def __str__(self) -> str:
        return self.title
    

class QHSEVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='HSE Video/%Y/%m/%d/')


    class Meta:
        verbose_name_plural  = "HSE Videos"



    def __str__(self) -> str:
        return self.title
    

    
class QHSEImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='HSE Image/%Y/%m/%d/')


    class Meta:
        verbose_name_plural  = "HSE Images"



    def __str__(self) -> str:
        return self.title
    


class Exploration(models.Model):
    title_en = models.CharField(max_length=100)
    content_en = models.TextField(max_length=3000)
    title_ar = models.CharField(max_length=100)
    content_ar = models.TextField(max_length=3000)
    image = models.FileField(upload_to='Operation Image/%Y/%m/%d/')


    class Meta:
        verbose_name_plural  = "Exploration"

    def __str__(self) -> str:
        return self.title_en
    


class Drilling(models.Model):
    title_en = models.CharField(max_length=100)
    content_en = models.TextField(max_length=3000)
    title_ar = models.CharField(max_length=100)
    content_ar = models.TextField(max_length=3000)
    image = models.FileField(upload_to='Operation Image/%Y/%m/%d/')


    class Meta:
        verbose_name_plural  = "Drilling Activities"

    def __str__(self) -> str:
        return self.title_en
    


class PetroleumEngineering(models.Model):
    title_en = models.CharField(max_length=100)
    content_en = models.TextField(max_length=3000)
    title_ar = models.CharField(max_length=100)
    content_ar = models.TextField(max_length=3000)
    image = models.FileField(upload_to='Operation Image/%Y/%m/%d/')


    class Meta:
        verbose_name_plural  = "Petroleum Engineering Activities"

    def __str__(self) -> str:
        return self.title_en
    

class ICT(models.Model):
    title_en = models.CharField(max_length=100)
    content_en = models.TextField(max_length=3000)
    title_ar = models.CharField(max_length=100)
    content_ar = models.TextField(max_length=3000)
    image = models.FileField(upload_to='ICT Image/%Y/%m/%d/')


    class Meta:
        verbose_name_plural  = "ICT"

    def __str__(self) -> str:
        return self.title_en
