from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400, blank=True)
    banner = models.ImageField(upload_to="uploads/store/categories/%Y/%m/%d/", blank=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def _generate_unique_slug(self):
        slug = slugify(self.name)
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=400, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)
    image = models.ImageField(upload_to="uploads/store/products/%Y/%m/%d/", blank=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    def __str__(self):
        return self.name

    def _generate_unique_slug(self):
        slug = slugify(self.name)
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super(Product, self).save(*args, **kwargs)
    