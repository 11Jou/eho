from django.db import models

# Create your models here.

class New(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title_en = models.CharField(max_length=500)
    content_en = models.TextField(max_length=5000)
    title_ar = models.CharField(max_length=500)
    content_ar = models.TextField(max_length=5000)
    cover = models.ImageField(upload_to='news/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    

class NewsImage(models.Model):
    related_news = models.ForeignKey(New, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y/%m/%d/')


    
    class Meta:
        verbose_name_plural  = "News Images"


    def __str__(self) -> str:
        return str(self.related_news)
    



class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title_en = models.CharField(max_length=500)
    content_en = models.TextField(max_length=5000)
    title_ar = models.CharField(max_length=500)
    content_ar = models.TextField(max_length=5000)
    cover = models.ImageField(upload_to='events/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    

class EventVideo(models.Model):
    related_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    video = models.FileField(upload_to='events/%Y/%m/%d/', null=True, blank=True)

    
    class Meta:
        verbose_name_plural  = "Events Videos"


    def __str__(self) -> str:
        return str(self.related_event)
    


class Departement(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.name


class Career(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resume/%Y/%m/%d/')

    
    class Meta:
        verbose_name_plural  = "Career"


    def __str__(self) -> str:
        return f"{str(self.name)} - {str(self.departement)}"
    

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField(max_length=200)

    
    class Meta:
        verbose_name_plural  = "Messages"


    def __str__(self) -> str:
        return self.name

    