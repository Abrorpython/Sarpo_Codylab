from django.db import models


class Income(models.Model):
    income = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Kirim summasi')
    descriptions = models.TextField(verbose_name="Ma'lumot")
    data = models.DateField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.data)} sanada {self.income} kirim bo'lgan"

    class Meta:
        ordering = ['-date']
        verbose_name = 'Kirimlar'
        verbose_name_plural = 'Kirim'


class Expense(models.Model):
    expense = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Chiqim summasi')
    descriptions = models.TextField(verbose_name="Ma'lumot")
    data = models.DateField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.data)} sanada {self.expense} chiqim bo'lgan"

    class Meta:
        ordering = ['-date']
        verbose_name = 'Chiqimlar'
        verbose_name_plural = 'Chiqim'
