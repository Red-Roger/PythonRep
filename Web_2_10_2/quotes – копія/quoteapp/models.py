from django.db import models


class Authors(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=150, null=False)
    born_location = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=150, null=False)

    def __str__(self):
        return f"{self.fullname}"

class Quotes(models.Model):
    tags = models.CharField(max_length=50, null=False)
    author = models.ManyToManyField(Authors)
    quote = models.CharField(max_length=150, null=False)

    def __str__(self):
        return f"{self.tags}"

