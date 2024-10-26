from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=255, blank=False, null=False)
    cellphone = models.CharField(
        max_length=20, blank=False, null=False, default='(00) 00000-0000'
    )
    car_model = models.CharField(
        max_length=255, blank=False, null=False, default=''
    )
    car_plate = models.CharField(
        max_length=255, blank=False, null=False, default=''
    )
    is_store = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return f'Register of {self.client_name}'
