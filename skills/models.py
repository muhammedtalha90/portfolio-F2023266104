from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('professional', 'Professional'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='technical')
    proficiency = models.IntegerField(default=80, help_text="Percentage (0-100)")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', '-proficiency']
