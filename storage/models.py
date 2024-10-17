from django.db import models  # type:ignore


class CategoryStorage(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return str(self.name)


class Storage(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    category = models.ForeignKey(to=CategoryStorage, on_delete=models.PROTECT)
    detail = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return str(self.name)
