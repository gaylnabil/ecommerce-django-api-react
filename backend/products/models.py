from django.db import models

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField, ImageSpecField
from django.utils.translation import gettext as _

from products.utils import resize_image, Mode

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from rest_framework.reverse import reverse

# from django.conf import settings
# User = settings.AUTH_USER_MODEL

# Create Category models.


class Category(models.Model):
    # TYPES = (
    #     ('adventurer', _('Adventurer')),
    #     ('climber', _('Climber')),
    # )
    TYPES = (
        ('Desktop', 'Desktop'),
        ('Laptop', 'Laptop'),
    )

    name = models.CharField(max_length=150, blank=False,
                            null=False, choices=TYPES, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        dictionary = dict(self.TYPES)
        return dictionary[self.name]

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'categories'


# Create Product models QuerySet.
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        print('USER QUERYSET:', user)
        return (
            self.is_public().filter(lookup)
            if user is None
            else self.filter(lookup, user=user)
        )
        # return (
        #     qs.filter(lookup)
        #     if user is None else
        #     (self.filter(lookup, user=user) |
        #      qs.filter(lookup, user=user)).distinct()
        # )

# Create Product models Manager.


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

# Create Product models.


class Product(models.Model):

    title = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    description = models.TextField(max_length=5000, blank=True, null=True)

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=10.99
    )

    # product_image = ProcessedImageField(
    #     upload_to='uploads/%Y/%m/%d/',
    #     default='/uploads/default.png',
    #     processors=[ResizeToFill(370, 477)],
    #     format='JPEG',
    #     options={'quality': 100},
    #     max_length=500,
    #     blank=True,
    #     null=True
    # )

    # thumbnail = ImageSpecField(
    #     source='product_image',
    #     processors=[ResizeToFill(180, 180)],
    #     format='JPEG',
    #     options={'quality': 100}
    # )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='categories',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        default=1
    )

    public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return '%.2f' % (float(self.price) * 0.8)

    def get_discount(self):
        return '10%'

    def is_public(self):
        return self.public  # return True or False

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})

    @property
    def endpoint(self):
        return self.get_absolute_url()
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     print("this is my image :", self.product_image)
    #     if self.product_image and self.product_image != '/uploads/default.png':
    #         img = resize_image(self.product_image.path, (370, 477), Mode.ZOOM)
    #         img.save(self.product_image.path, quality=100)

    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'product'
        verbose_name_plural = 'products'
