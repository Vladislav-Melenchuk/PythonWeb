from django.db import models

class Expense(models.Model):
    title = models.CharField("Назва", max_length=200)
    amount = models.DecimalField("Сума", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
