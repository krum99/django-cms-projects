from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.core.validators import MinValueValidator

class MasterCardsContainer(CMSPlugin):
    title = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title or "MasterCards Container"


class MasterCardInfo(CMSPlugin):
    title = models.CharField(max_length=128)

    # credit limit range: (min, max)
    credit_limit_min = models.PositiveIntegerField(
        verbose_name="Credit limit (min)",
        validators=[MinValueValidator(1)],
    )
    credit_limit_max = models.PositiveIntegerField(
        verbose_name="Credit limit (max)",
        validators=[MinValueValidator(1)],
    )

    no_rate_period = models.PositiveIntegerField(
        verbose_name="Grace period (days)",
        validators=[MinValueValidator(1)],
    )

    gdr = models.DecimalField(
        verbose_name="Annual interest rate (%)",
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    year_tax = models.DecimalField(
        verbose_name="Annual fee",
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    is_default = models.BooleanField(
    default=False,
    help_text="Which card loads by default"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.is_default and self.parent_id:
            MasterCardInfo.objects.filter(
                parent_id=self.parent_id
            ).exclude(pk=self.pk).update(is_default=False)


    def __str__(self):
        return self.title or "Master Card"