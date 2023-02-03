from django.utils import timezone
from django.db import models
from PIL import Image


class Product(models.Model):
    CLOTHES = 'clothes'
    SHOES = 'shoes'
    SKATES = 'skates'
    ACC = 'accessories'

    CHOICE_GROUP = {
        (CLOTHES, 'clothes'),
        (SHOES, 'shoes'),
        (SKATES, 'skates'),
        (ACC, 'accessories'),
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.CharField(max_length=8, default='One size')
    price = models.IntegerField()
    availability = models.BooleanField(default=True)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=CLOTHES)
    img = models.ImageField(default='no-image.jpg', upload_to='product_image')

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.title}/'

    class Meta:
        ordering = ('-publish', )


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Review by {} on {}'.format(self.name, self.product)
