from django.db import models
import os, datetime, random


class Category(models.Model):
    name = models.CharField('Kategoriya', max_length=255)
    date = models.CharField(max_length=32)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-data']
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


def upload_file_name(instance, filename):
    _, ext = os.path.splitext(filename)

    return "{}/{}{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
        instance.upload_folder,
        datetime.datetime.now().strftime("%Y%m"),
        datetime.datetime.now(), random.randint(1000, 9999), ext)


class Product(models.Model):

    PARAMETR_CHOICE = [

        ("metr", "metr"),
        ("dona", "dona"),
        ("kg", "kg")

    ]
    upload_folder = 'post'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Kategoriya nomi')
    name = models.CharField(verbose_name='Mahsulot nomi', max_length=255)
    parametr = models.CharField(verbose_name='Mahuslot birligi', choices=PARAMETR_CHOICE, max_length=32)
    image = models.ImageField(verbose_name='Mahsulot rasmi', upload_to=upload_file_name, default='posts/default.jpg')
    qr = models.CharField(verbose_name='Q/R', max_length=255)
    amount = models.FloatField(verbose_name='Mahsulot miqdori')
    sel_price = models.FloatField(verbose_name='Olingan narx')
    finish_price = models.FloatField(verbose_name='Sotiladigan oxirgi narx')
    date = models.CharField(verbose_name="Mahsulot qo'shilgan vaqt", max_length=32)
    descriptions = models.TextField(verbose_name="Mahsulot haqida ma'lumot")
    status = models.BooleanField(verbose_name='Status', default=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.id)} | {self.name}"

    class Meta:
        ordering = ['-data']
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'


class Customer(models.Model):
    name = models.CharField(verbose_name='F.I.Sh', max_length=255)
    number = models.CharField(verbose_name='Tel Number', max_length=32)
    descriptions = models.TextField(verbose_name="Mijoz haqida ma'lumot")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.id)} | {self.name}"

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'

