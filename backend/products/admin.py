from django.contrib import admin
from products.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields(
    ) if field.name != 'description']

    class Meta:
        model = Product
        # fieldsets = (
        #     (None, {
        #         "fields": (

        #         ),
        #     }),
        # )
