# Generated by Django 5.0.3 on 2024-06-24 12:46

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
                ('special_offer', models.BooleanField(default=False, verbose_name='Специальное предложение')),
                ('short_description', models.TextField(verbose_name='Короткое описание')),
                ('expires_in', models.DateField(verbose_name='Дата окончания')),
                ('percentage', models.PositiveSmallIntegerField(verbose_name='Процент скидки')),
                ('in_discount', models.BooleanField(default=False, verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
        migrations.CreateModel(
            name='ActionTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Тэг акции',
                'verbose_name_plural': 'Тэги акции',
            },
        ),
        migrations.CreateModel(
            name='ContactChiefDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('full_name', models.CharField(max_length=120, verbose_name='Ф.И.О')),
                ('message', models.TextField(verbose_name='Обращение')),
                ('active', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Обращение к глав. Врачу',
                'verbose_name_plural': 'Обращении к глав. Врачу',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('work_time', models.CharField(max_length=120, verbose_name='Рабочее время')),
                ('telegram', models.URLField(verbose_name='Телеграм')),
                ('instagram', models.URLField(verbose_name='Инстаграм')),
                ('facebook', models.URLField(verbose_name='Фейсбук')),
                ('vkontakte', models.URLField(verbose_name='Вконтакте')),
                ('location', models.URLField(verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='OnlineAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('full_name', models.CharField(max_length=120, verbose_name='Ф.И.О')),
                ('book_date', models.DateField(verbose_name='Дата записи')),
                ('active', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Онлайн заявка',
                'verbose_name_plural': 'Онлайн заявки',
            },
        ),
        migrations.CreateModel(
            name='PhotoGalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория фотогалереи',
                'verbose_name_plural': 'Категории фотогалереи',
            },
        ),
        migrations.CreateModel(
            name='ActionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_images', to='clinics.action', verbose_name='Акция')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото акции',
                'verbose_name_plural': 'Фото акции',
            },
        ),
        migrations.AddField(
            model_name='action',
            name='tags',
            field=models.ManyToManyField(blank=True, to='clinics.actiontag', verbose_name='Тэги'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('full_name', models.CharField(max_length=120, verbose_name='Ф.И.О')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_view', models.BooleanField(default=True, verbose_name='Показывается ли на сайте')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория новостей',
                'verbose_name_plural': 'Категории новостей',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
                ('desc', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('special_offer', models.BooleanField(default=False, verbose_name='Является ли спец. предложением')),
                ('published', models.BooleanField(default=False, verbose_name='Показано ли на сайте')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.newscategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.photogallerycategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Фотография галереи',
                'verbose_name_plural': 'Фотографии галереи',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='Ф.И.О')),
                ('position', models.CharField(max_length=120, verbose_name='Позиция в клинике')),
                ('about', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Про врача коротко')),
                ('certificates', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Сертификаты врача')),
                ('experience_in_company', models.CharField(max_length=120, verbose_name='Опыт работы в клинике')),
                ('experience_in_field', models.CharField(max_length=120, verbose_name='Опыт работы в этой области')),
                ('experience_in_years', models.CharField(max_length=120, verbose_name='Опыт работы в годах')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
            },
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Файл диплома')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diploma', to='clinics.specialist', verbose_name='Врач к которому принадлежит диплом !')),
            ],
            options={
                'verbose_name': 'Диплом',
                'verbose_name_plural': 'Дипломы',
            },
        ),
        migrations.CreateModel(
            name='StoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория сторисов',
                'verbose_name_plural': 'Категории сторисов',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
                ('order', models.IntegerField(verbose_name='Порядок')),
                ('published', models.BooleanField(default=False, verbose_name='Показывается ли на сайте')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='Фото или гиф')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.storycategory', verbose_name='Категория сториса')),
            ],
            options={
                'verbose_name': 'Сторис',
                'verbose_name_plural': 'Сторисы',
            },
        ),
        migrations.CreateModel(
            name='StoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='products.product')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='clinics.story')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Наименование')),
                ('responsibilities', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Обязанности')),
                ('requirements', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Требования')),
                ('conditions', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Условия')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
