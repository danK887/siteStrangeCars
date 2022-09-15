from django.db import models
from django.urls import reverse


class Cars(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%d/%m/%Y/")
    time_create = models.DateTimeField(auto_now_add=True)
    categor = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Странная машина'
        verbose_name_plural = 'Странные машины'
        ordering = ['-time_create', 'title']

class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('categories', kwargs={'categor_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
