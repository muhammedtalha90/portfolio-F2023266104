from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['-start_year']
