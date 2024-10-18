from django.db import models


class ServiceOrder(models.Model):
    client_name = models.CharField(max_length=255, blank=False, null=False)
    client_cellphone = models.CharField(max_length=255, blank=False, null=False)
    car_model = models.CharField(max_length=255, blank=False, null=False)
    car_plate = models.CharField(max_length=10, blank=False, null=False)

    service_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False
    )

    service = models.CharField(max_length=255, blank=False, null=False)

    paid = models.BooleanField(
        blank=False, null=False, verbose_name="Payment Made",
        editable=True
    )
    created_at = models.DateField(auto_now_add=True)

    observation = models.CharField(max_length=255, null=True, blank=True)

    cpf = models.CharField(max_length=18, null=True, blank=True)

    class Meta:
        ordering = ['-id']
