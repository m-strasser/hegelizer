from django.db import models


class NotionModel(models.Model):
    """Model representation of the Notion class"""
    name = models.CharField(max_length=50)
    hegelian_type = models.CharField(max_length=30)


class OtherNameModel(models.Model):
    """Stores an alternative name (other name) for a Notion."""
    notion = models.ForeignKey(NotionModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    notes = models.TextField()


class DialecticModel(models.Model):
    """Model representation of the Dialectic class"""
    root = models.ForeignKey(NotionModel, on_delete=models.CASCADE)
    path1 = models.ForeignKey(NotionModel, on_delete=models.CASCADE,
                              related_name='path_1')
    path2 = models.ForeignKey(NotionModel, on_delete=models.CASCADE,
                              related_name='path2')
