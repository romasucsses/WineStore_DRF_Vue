from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=55)
    stars_count = models.IntegerField(null=True)
    review = models.TextField()
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, default=None)
    date = models.DateField(auto_now=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=355)
    image = models.ImageField(upload_to="img/%y/%m/%d/")
    price = models.FloatField()
    category = models.ForeignKey('products.ProductCategory', on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    slug_url = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name
