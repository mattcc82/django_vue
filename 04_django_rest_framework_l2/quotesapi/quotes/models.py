from django.db import models


class Quotes(models.Model):
    quote_author = models.CharField(max_length=60)
    quote_body = models.TextField()
    context = models.CharField(max_length=60)
    source = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quotes'
        verbose_name_plural = 'Quotes'

    def __str__(self):
        return super().__str__()
