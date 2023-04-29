import uuid

from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Category model.
    """

    class Meta:
        verbose_name_plural = "categories"

    class JSONAPIMeta:
        resource_name = "category"

    class Type(models.TextChoices):
        CHARACTER = "character"
        SETTING = "setting"
        FORMAT = "format"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(
        max_length=256,
        help_text="A short description that describes when this category applies.",
    )

    type = models.CharField(max_length=9, choices=Type.choices, null=True)

    is_nsfw = models.BooleanField(
        default=False,
        null=False,
        help_text="Wether the name or description of the category contain NSFW content or not.",
        verbose_name="Is NSFW",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
