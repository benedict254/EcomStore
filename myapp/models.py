from django.db import models

# Create your models here.
class slider(models.Model):
	title = models.CharField(max_length=255)
	desc  = models.TextField()
	image = models.ImageField(upload_to='slider')

	def __str__(self):
		return self.title


CATEGORY_CHOICES = (
	('S','Shoe'),
	('E','Electronics'),
	('F','Food'),
	('M','Men'),
	('B','Books'),
	('C','Cars')
)


class Item(models.Model):
	title = models.CharField(max_length=200)
	category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
	description = models.TextField()
	slug =  models.SlugField(default='F')
	image = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=100,default='default.jpg')

	def __str__(self):
		return self.category

	def get_total_cars(self):
		return self.category.C


class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name