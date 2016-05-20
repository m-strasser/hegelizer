from django.db import models


class Notion(models.Model):
    """Model representation of the Notion class"""
    name = models.CharField(max_length=50)
    hegelian_type = models.CharField(max_length=30)


class OtherName(models.Model):
    """Stores an alternative name (other name) for a Notion."""
    notion = models.ForeignKey(Notion, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    notes = models.TextField()


class Dialectic(models.Model):
    """Model representation of the Dialectic class"""
    root = models.ForeignKey(Notion, on_delete=models.SET_NULL)
    path1 = models.ForeignKey(Notion, on_delete=models.SET_NULL)
    path2 = models.ForeignKey(Notion, on_delete=models.SET_NULL)
