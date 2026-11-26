from django.db import models
from django.contrib.auth.models import User


class Opportunity(models.Model):
    title_ar = models.CharField(max_length=140)
    title_en = models.CharField(max_length=140)
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=40)
    location_ar = models.CharField(max_length=100)
    location_en = models.CharField(max_length=100)
    description_ar = models.TextField()
    description_en = models.TextField()
    is_remote = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.company} — {self.title_en}"


class Profile(models.Model):
    ROLE_CHOICES = [("learner", "Learner"), ("mentor", "Mentor")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default="learner")
    headline = models.CharField(max_length=160, blank=True)

    def __str__(self):
        return self.user.username


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name="applications")
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "opportunity"], name="unique_opportunity_application")]
        ordering = ["-created_at"]
