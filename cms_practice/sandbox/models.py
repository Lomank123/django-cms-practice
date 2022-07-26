from django.db import models
from cms.models.fields import PlaceholderField


class MyModel(models.Model):
    my_placeholder = PlaceholderField('My model')
