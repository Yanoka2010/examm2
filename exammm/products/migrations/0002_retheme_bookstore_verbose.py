import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={
                'ordering': ['name'],
                'verbose_name': 'Раздел каталога',
                'verbose_name_plural': 'Разделы каталога',
            },
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={
                'ordering': ['name'],
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={
                'ordering': ['name'],
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название раздела'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название издательства'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(
                on_delete=models.deletion.CASCADE,
                to='products.category',
                verbose_name='Раздел каталога',
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Аннотация'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='products/',
                verbose_name='Обложка',
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(
                on_delete=models.deletion.CASCADE,
                to='products.manufacturer',
                verbose_name='Издательство',
            ),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(
                default=0,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name='Остаток на складе (экз.)',
            ),
        ),
    ]
