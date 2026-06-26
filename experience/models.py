from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default='Present')
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.organization}"

    class Meta:
        ordering = ['-start_date']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
