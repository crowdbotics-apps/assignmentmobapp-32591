from django.conf import settings
from django.db import models


class Subscription(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscription_user",
    )
    plan = models.OneToOneField(
        "home.Plan",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_plan",
    )
    app = models.OneToOneField(
        "home.App",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subscription_app",
    )
    active = models.BooleanField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )


class App(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    type = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    framework = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    domain_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    screenshot = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    subscription = models.OneToOneField(
        "home.Subscription",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="app_subscription",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="app_user",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )


class Plan(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=20,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
