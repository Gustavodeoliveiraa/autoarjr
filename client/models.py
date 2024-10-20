from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=255, blank=False, null=False)
    cellphone = models.CharField(
        max_length=20, blank=False, null=False, default=''
    )
    car_model = models.CharField(
        max_length=255, blank=False, null=False, default=''
    )
    car_plate = models.CharField(
        max_length=255, blank=False, null=False, default=''
    )
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return f'Register of {self.client_name}'
