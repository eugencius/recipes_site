import string

from django.db import models
from random import SystemRandom
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    # Representa o model que queremos encaixar no model Tag
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    # Representa o ID da linha do model
    object_id = models.CharField(max_length=255)

    # Este campo representa o objeto da Model que estamos utilizando na ForeignKey
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(
                    string.ascii_letters + string.digits,
                    k=5
                )
            )
            self.slug = slugify(f'{self.name}-{rand_letters}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
