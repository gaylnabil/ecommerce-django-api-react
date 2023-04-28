from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


def validate_title(value):
    """
    Validates that the title of a product is not empty and does not already exist in the database.
    Args:
        self: The instance of the serializer.
        value (str): The title to be validated.
    Returns:
        str: The validated title.
    Raises:
        serializers.ValidationError: If the title is None or already exists in the database.
    """
    if value is None:
        raise serializers.ValidationError("Title cannot be empty")
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(
            f"Product is already associated with ''{value}''")

    return value


unique_product_title = UniqueValidator(
    queryset=Product.objects.all(),
    lookup='iexact',
    message="Product must be unique: Product is already associated with",
)
